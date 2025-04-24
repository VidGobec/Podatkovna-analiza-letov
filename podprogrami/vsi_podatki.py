import json


try:
    with open("podatki_svet.json", "r") as dat:
        content = dat.read().strip()
        obstojeci_podatki = json.loads(content) if content else []
except (FileNotFoundError, json.JSONDecodeError):
    obstojeci_podatki = []

try:
    with open("podatki_evropa.json", "r") as dat:
        content = dat.read().strip()
        obstojeci_podatki_2 = json.loads(content) if content else []
except (FileNotFoundError, json.JSONDecodeError):
    obstojeci_podatki_2 = []
obstojeci_podatki.extend(obstojeci_podatki_2)

with open("vsi_podatki.json", "w") as dat:
    json.dump(obstojeci_podatki, dat, ensure_ascii=False, indent=2)

print("Nalaganje podatkov je končano!")