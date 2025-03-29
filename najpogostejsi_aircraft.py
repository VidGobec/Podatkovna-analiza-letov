import json

with open("vsi_podatki.json", "r") as dat:
    data = json.load(dat)

n = len(data)
aircrafts = {}
for let in data:
    aircraft = let["aircraft"]
    if aircraft:
        aircraft = aircraft["iata"]
        if aircraft in aircrafts:
            aircrafts[aircraft] += 1
        else:
            aircrafts[aircraft] = 1
    else:
        if "None" in aircrafts:
            aircrafts["None"] += 1
        else:
            aircrafts["None"] = 1

if "None" in aircrafts:
    ni_podatka = round((aircrafts["None"]/n)*100, 1)
    print(f"Ni podatka za približno {ni_podatka}% vseh letov!")
aircrafts.pop("None", None)

aircraft_max = max(aircrafts, key=aircrafts.get)
procenti = round((aircrafts[aircraft_max] / sum(aircrafts.values()))*100, 1)
print(f"Največ letov je bilo opravljeno z {aircraft_max} ({aircrafts[aircraft_max]}), kar je {procenti}% vseh letov, ki imajo na voljo podatek.")