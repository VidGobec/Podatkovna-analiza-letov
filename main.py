import json, requests
import iata 



#dodajanje_podatkov = input("Ali želiš dodati podatke (Da/Ne)?: ")
print("IATA koda letališča je tridigitalna oznaka, s katero se letališča enostavno identificirajo po svetu. IATA kodo izbranega letališča lahko najdeš tudi tukaj: https://www.iata.org/en/publications/directories/code-search/")
iata_input = input("Vpiši iato kodo od letališča: ")
if iata.iata(iata_input):
    novi_podatki = []
    params = {"access_key": "62905fc234eca138b48941106dcc9e98", "dep_iata": iata_input}
    res = requests.get("https://api.aviationstack.com/v1/flights", params=params)
    podatki = res.json()["data"]
    novi_podatki.extend(podatki)
    try:
        with open("vsi_podatki.json", "r") as dat:
            content = dat.read().strip()
            obstojeci_podatki = json.loads(content) if content else []
    except (FileNotFoundError, json.JSONDecodeError):
        obstojeci_podatki = []
    obstojeci_podatki.extend(novi_podatki)

    with open("vsi_podatki.json", "w") as dat:
        json.dump(obstojeci_podatki, dat, ensure_ascii=False, indent=2)

    print(novi_podatki)
    print("Nalaganje podatkov je končano!")
#print("Prišlo je do napake pri pridobivanju podatkov!") #Če so requesti že porabljeni
else:
    print("Vpiši veljavno IATA kodo!")


