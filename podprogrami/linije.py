import json, random
from poizvedbe import poizvedbe
import matplotlib.pyplot as plt

with open('vsi_podatki.json', 'r') as file:
    data = poizvedbe(json.load(file))
with open('vsa_letalisca.json', 'r') as file:
    data_letalisca = json.load(file)

import geopandas
import geodatasets
fig, ax = plt.subplots()
path = geodatasets.get_path("naturalearth.land")
df = geopandas.read_file(path)
ax = df.plot(ax=ax, figsize=(10, 10), alpha=0.5, edgecolor="k") #ax=ax da ne naredi novega okna

poti = {}
for let in data.get_data():
    letalisce1 = let["departure"]["airport"]
    letalisce2 = let["arrival"]["airport"]
    letalska_druzba = let["airline"]["name"]
    try:
        pot = tuple(sorted([letalisce1,letalisce2])+ [letalska_druzba]) #sortiramo da stejemo povezave iz x->y enako kot x<-y 
    except:
        print("========",letalisce1,"<->",letalisce2,f"[{letalska_druzba}]","========")
        continue
    if pot in poti:
        poti[pot] += 1
    else:
        poti[pot] = 1

najvec_letov = max(poti.values())

rgb_letalske_druzbe = {}
for let in data.get_data():
    letalska_druzba = let["airline"]["name"]
    rgb = (random.random(), random.random(), random.random())
    if rgb not in rgb_letalske_druzbe.values():
        rgb_letalske_druzbe[letalska_druzba] = rgb

for letalisca, stevilo in poti.items():
    xi = []
    yi = []
    letalisce1, letalisce2, letalska_druzba = letalisca
    letalisca = (letalisce1, letalisce2)
    for letalisce in letalisca:
        xi = xi + [float(x["longitude"]) for x in data_letalisca if x["airport_name"]==letalisce]
        yi = yi + [float(x["latitude"]) for x in data_letalisca if x["airport_name"]==letalisce]
        

    intenz = stevilo/najvec_letov
    r, g, b = rgb_letalske_druzbe[letalska_druzba]
    if intenz > 0.1:
        ax.plot(xi,yi, color = (r,g,b,intenz))
        

plt.show()
