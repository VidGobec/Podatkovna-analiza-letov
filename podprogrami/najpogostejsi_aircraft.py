import json

with open("podatki_evropa.json", "r") as dat:
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
print(f"https://www.google.com/search?sca_esv=36d1bc09254dbabd&sxsrf=AHTn8zqsK7K3tqIs91PS6nACzIEe8qBn1w:1743290931587&q=aircraft+iata+code+{aircraft_max}&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0")