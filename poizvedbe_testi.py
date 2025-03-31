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



import matplotlib.pyplot as plt
fig, ax = plt.subplots()

with open('test.json', 'r') as file:
    data_letalisa = json.load(file)["data"]


x = [float(x["longitude"]) for x in data_letalisa]
y = [float(x["latitude"]) for x in data_letalisa]

ax.scatter(x, y, s=15, c="blue", vmin=0, vmax=100)


plt.show()