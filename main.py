import json, requests, time
from podprogrami import iata



print("\n 〰〰〰️✈︎ Dobrodošli v programu za iskanje letalskih statistik in najboljših letov! 〰〰〰〰\n")
time.sleep(0.5)
print("\nNekaj splošnih informacij!\n")
time.sleep(0.5)
print("- V programu uporabljamo IATO kodo.")
niz = "IATA koda letališča je tridigitalna oznaka, s katero se letališča enostavno identificirajo po svetu. IATA kodo izbranega letališča lahko najdeš tudi tukaj: https://www.iata.org/en/publications/directories/code-search/".split()
for beseda in niz:
    print(beseda, end=' ', flush=True)
    time.sleep(0.07)

time.sleep(0.7)
print("\n\n- Iz seznama izbereš številko, tistega, kar želiš, da se izvede s nizom, pri čemer so številke ločene z vejico (npr. '1,3,4')")
print("\nSedaj pa izberi iz seznama!")
print("\n1 - statistika letov po svetu\n2 - statistika letov po evropi\n3 - dodajanje podatkov k statistiki\n4 - iskalnik letov\n5 - iskalnik letov iz bližnjih letališč\n")
izbira = input("Vnesi številke iz seznama (ločene z vejico): ")
try:
    izbira = izbira.split(",")
    izbira = [int(st) for st in izbira]
    print(izbira)
except ValueError:
    izbira = [int(izbira)]
    print(izbira)

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
        print("\nNalaganje podatkov je končano!\n")
#print("Prišlo je do napake pri pridobivanju podatkov!") #Če so requesti že porabljeni
    else:
        print("\nVpiši veljavno IATA kodo!\n")

pridobivanje_statistike = input("Ali želiš pridobiti statistiko letov po svetu ali Evropi (Da/Ne)?: ").capitalize()
samo_evropa = input("Ali želiš podatke samo za Evropo (Da/Ne): ").capitalize()
if samo_evropa == "Da":
    print("ok")
else:
    if pridobivanje_statistike == "Da":
        izbira = input("\nIzberi iz seznama tako, da izbereš številko kaj želiš prikazati, če želiš več loči z vejico:\n0 - model letala\n1 - letalske družbe\n2 - prikaz povezav").split(",")
        for x in izbira:
            if x == 0:
                print("ok")
