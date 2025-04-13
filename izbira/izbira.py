import json
import matplotlib.pyplot as plt
import math
import random
import requests

with open(f"googleleti.json", "r") as dat:
    data = json.load(dat)




#uporabnik vnese preferenco
def vnos_preference() -> dict:
    """funkcija vprasa uporabnika po preferencah in jih vrne, kot seznam"""
    default_preferenca = {
    "cena": 1,
    "celoten cas" : 0,
    "cas v zraku" : 0,
    "cas med leti" : 0,
    "karbonske emisije": 0
    }
    preferenca = dict()
    while len(preferenca) < len(default_preferenca):
        for pref in default_preferenca:
            try:
                inp = float(input(f"vpisite preferenco za {pref}: "))
                preferenca[pref] = inp
            except:
                print("prosim vnesite stevilo.")
                break

    return preferenca
            

preferenca = vnos_preference()
try:
    ura_zadnja_kul = float(input("vnesi najvecji cas prestopa. (default 8): "))
except:
    ura_zadnja_kul = 8
odklon = math.sqrt(-(ura_zadnja_kul - 3)**2 / (2 * math.log(0.01)))

data_letov = data["best_flights"]


#kreiranje tabele za primerjanje
#mogoce spremeni v funkcijo kjer klices request
tabela_primerjanj = [] #predstavlja tabelo kjer so vrstice informacije(cena,cas..) stolpci pa specificni leti (prvi lement tabele je tabela cen letov)

tabela_primerjanj.append([x["price"] for x in data_letov])

tabela_primerjanj.append([sum([let["duration"] for let in x["flights"]]) for x in data_letov])

tabela_primerjanj.append([[let["duration"] for let in x["layovers"]] for x in data_letov])

pom = [sum([let["duration"] for let in x["flights"]]) for x in data_letov]
zdr = [x + y for x, y in zip(tabela_primerjanj[1], pom)]
tabela_primerjanj.insert(1, list(zdr))

tabela_primerjanj.append([x["carbon_emissions"]["this_flight"] for x in data_letov])


def linearen_utility(cena, min, max):
    """linarno padajoca funkcija"""
    return 1 - (cena - min) / (max - min)

def cas_prestopanja(prestopanje, ideal = 3, odklon = 8):
    """funkcija ki je 0 za ure < 2 povsod drugje pa je gavsovo porazdeljena z srediscem v 3 (najvecja vrednost je 1)"""
    prestopanje = prestopanje/60 #pretvorba v ure
    if prestopanje < 2:
        return 0

    return math.exp(-(pow((prestopanje - ideal),2)) / (2 * pow(odklon,2)))


#ocene
st_vseh_opcij = len(data_letov)
ocene = [0]*len(tabela_primerjanj[0])

##ocena cene
minv = min(tabela_primerjanj[0])
maxv = max(tabela_primerjanj[0])
i = 0
while i < st_vseh_opcij:
    ocene[i] += linearen_utility(tabela_primerjanj[0][i], minv, maxv) * preferenca["cena"]
    i += 1

print("ocena cen")
print(ocene)
print(tabela_primerjanj[0])

##ocena celotnega casa
minv = min(tabela_primerjanj[1])
maxv = max(tabela_primerjanj[1])
i = 0
while i < st_vseh_opcij:
    ocene[i] += linearen_utility(tabela_primerjanj[1][i], minv, maxv) * preferenca["celoten cas"]
    i += 1

print("+ocena celotnega casa")
print(ocene)
print(tabela_primerjanj[1])

##cas v zraku
minv = min(tabela_primerjanj[2])
maxv = max(tabela_primerjanj[2])
i = 0
while i < st_vseh_opcij:
    ocene[i] += linearen_utility(tabela_primerjanj[2][i], minv, maxv) * preferenca["cas v zraku"]
    i += 1

print("+ocena casa v zraku")
print(ocene)
print(tabela_primerjanj[2])

##cas med leti

i = 0
while i < st_vseh_opcij:
    st_prestopov = len(tabela_primerjanj[3][i])
    for cas in tabela_primerjanj[3][i]:
        ocene[i] += (cas_prestopanja(cas, odklon = odklon) * preferenca["cas med leti"])/st_prestopov
    i += 1

print("+ ocena casa med leti")
print(ocene)
print(tabela_primerjanj[3])