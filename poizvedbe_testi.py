from poizvedbe import poizvedbe
import json

with open('podatki_svet.json', 'r') as file:
    data = json.load(file)


def povp_vrednost(tabela):
    """vrne povprecno vrednost stevil v tabeli"""
    return sum(x for x in tabela if x is not None)/len(tabela)

##tests
pristali = poizvedbe.get_pristali(data)
#print(pristali[0],"\n", pristali[1])
zamudniki = poizvedbe.get_zamudniki(pristali)
#print(zamudniki[0])
print("ce gledamo vse lete v podatki_svet")
zamudniki_ob_pristanku = poizvedbe.get_zamudniki_ob_pristaneku(data)
povp = povp_vrednost([x["arrival"]["delay"] for x in zamudniki_ob_pristanku])
print(f"povp vrednost zamude letal v odhodu je {povp}")

zamudniki_ob_odhodu = poizvedbe.get_zamudniki_ob_odhodu(data)
povp = povp_vrednost([x["departure"]["delay"] for x in zamudniki_ob_odhodu])
print(f"povp vrednost zamude letal v prihodu je {povp}")

##
print("\nce gledamo le pristale lete v podatki_svet\n")
print("ce gledamo vse lete v podatki_svet")
zamudniki_ob_pristanku = poizvedbe.get_zamudniki_ob_pristaneku(pristali)
povp = povp_vrednost([x["arrival"]["delay"] for x in zamudniki_ob_pristanku])
print(f"povp vrednost zamude letal v odhodu je {povp}")

zamudniki_ob_odhodu = poizvedbe.get_zamudniki_ob_odhodu(pristali)
povp = povp_vrednost([x["departure"]["delay"] for x in zamudniki_ob_odhodu])
print(f"povp vrednost zamude letal v prihodu je {povp}")

##
print("############################")
x = poizvedbe.get_vrednosti(pristali, ["departure","delay"])
povp = povp_vrednost(x)
print(f"povp vrednost zamude letal v prihodu je {povp}")



print("\n\n")
##graf letalisc in povprecnih zamud na letalisce
with open('podatki_svet.json', 'r') as file:
    data = poizvedbe(json.load(file))
with open('vsa_letalisca.json', 'r') as file:
    data_letalisa = json.load(file)

data_po_letaliscih = data.get_grouped_data(["departure","airport"])
tabela_zamud_po_letaliscih = []
for letalisce, leti in data_po_letaliscih.items():
    zamudniki = poizvedbe.get_zamudniki_ob_odhodu(leti)
    vsota_zamud = sum([x["departure"]["delay"] for x in zamudniki])
    povp_zamuda = vsota_zamud/len(leti)

    try:
        tabela_zamud_po_letaliscih.append([[float(x["longitude"]) for x in data_letalisa if x["airport_name"]==letalisce][0],
                                    [float(x["latitude"]) for x in data_letalisa if x["airport_name"]==letalisce][0],
                                    povp_zamuda])
    except:
        pass

print(tabela_zamud_po_letaliscih) 
#graf gostote zamujanja po letaliscih
import matplotlib.pyplot as plt
fig, ax = plt.subplots()


#background
import geopandas
import geodatasets
path = geodatasets.get_path("naturalearth.land")
df = geopandas.read_file(path)
ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")

#foregtound
tab_x = [x[0] for x in tabela_zamud_po_letaliscih]
tab_y = [x[1] for x in tabela_zamud_po_letaliscih]
skalar = 30 #za povecavo poprecja zamud na grafu
tab_povpzamuda = [x[2]*skalar for x in tabela_zamud_po_letaliscih]

ax.scatter(tab_x, tab_y, s=tab_povpzamuda, c="red", alpha = 0.3,edgecolors=None, vmin=0, vmax=100)
ax.scatter(tab_x, tab_y, s=15, c="blue", vmin=0, vmax=100)


plt.show()