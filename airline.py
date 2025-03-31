import json
import matplotlib.pyplot as plt
import time

with open("vsi_podatki.json", "r") as dat:
    data = json.load(dat)

n = len(data)
airlines = {}
for let in data:
    airline = let["airline"]
    if airline:
        airline_name = airline["name"]
        if airline_name in airlines:
            airlines[airline_name] += 1
        else:
            airlines[airline_name] = 1
    else:
        if "None" in airlines:
            airlines["None"] += 1
        else:
            airlines["None"] = 1


if None in airlines:
    ni_podatka = round((airlines[None]/n)*100, 1)
    print(f"Ni podatka za približno {ni_podatka}% vseh letov!")
airlines.pop(None, None)
airlines = dict(sorted(airlines.items(), key=lambda item: item[1], reverse=True))

plt.figure(figsize=(12, 6))
plt.bar(list(airlines.keys()), list(airlines.values()), color='b', edgecolor='w', width=5, linewidth=1)
plt.xticks(rotation=90, fontsize=2)
plt.title("Letalske družbe")
plt.show()


airline_max = max(airlines, key=airlines.get)
procenti = round((airlines[airline_max] / sum(airlines.values()))*100, 1)
print(f"Največ letov je bilo opravljeno z {airline_max} ({airlines[airline_max]}), kar je {procenti}% vseh letov, ki imajo na voljo podatek.")
print(f"https://www.google.com/search?sca_esv=36d1bc09254dbabd&sxsrf=AHTn8zqsK7K3tqIs91PS6nACzIEe8qBn1w:1743290931587&q=aircraft+iata+code+{airline_max}&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0")