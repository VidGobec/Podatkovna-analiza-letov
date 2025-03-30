import koordinate_iata as iata
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import random


evropa_iata = ["LHR", "IST", "CDG", "AMS", "MAD", "FRA", "BCN", "FCO", "LGW", "SVO", "MUC", "LIS", "DUB", "ATH", "VIE", "ZRH", "MXP", "OSL", "BRU", "WAW", "BUD", "ARN", "VCE", "NCE", "OTP", "HEL", "BEG", "KEF"]

with open("podatki_evropa.json", "r") as dat:
    data = json.load(dat)

fig = plt.figure()

leti = {}

for let in data:
    dep = let["departure"]
    arr = let["arrival"]
    lon_dep, lat_dep = iata.koordinate_iata(dep["iata"])
    lon_arr, lat_arr = iata.koordinate_iata(arr["iata"])

    if dep["airport"] in leti:
        slovarck = leti[dep["airport"]]
        slovarck["longitude_arr"].append(lon_arr)
        slovarck["latitude_arr"].append(lat_arr)
        leti[dep["airport"]] = slovarck
    else:
        podslovar = {}

        podslovar["longitude_dep"] = lon_dep
        podslovar["latitude_dep"] = lat_dep

        podslovar["longitude_arr"] = [lon_arr]
        podslovar["latitude_arr"] = [lat_arr]

        leti[dep["airport"]] = podslovar

plt.title("Leti po evropi")
fig.savefig('leti_po_evropi.png')
fig.show()