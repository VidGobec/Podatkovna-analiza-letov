from serpapi import GoogleSearch
import json
from izbiralec_letov import izbiralec_letov

letalisca1 = "LJU,KLU,GRZ,/m/04jpl"
letalisca = ["ZAG,TRS,TSF,/m/04jpl", "VCE,TRS,VIE,/m/04jpl", "SZG,LIN,MXP,/m/04jpl", "MUC,STR,FCO,/m/04jpl", "BUD,PRG,ZRH,/m/04jpl"]
destinacija = input("Vpiši iato kodo kam želiš leteti: ").upper()

datum = input("Vpiši termin (format: YYYY-MM-DD - YYYY-MM-DD): ")

try:
    odhod_datum, prihod_datum = datum.split(" - ")
except ValueError:
    print("Invalid date format. Please use the format YYYY-MM-DD - YYYY-MM-DD.")
    exit()

key = "9aa8f07a4838c4c78081cbafe35b26cd7389b628269b05fe8304a3e55f902c47"  

params = {
  "engine": "google_flights",
  "departure_id": letalisca1,
  "arrival_id": destinacija,
  "outbound_date": odhod_datum,
  "return_date": prihod_datum, 
  "currency": "EUR",
  "hl": "sl",
  "api_key": key
}

search = GoogleSearch(params)
results = search.get_json()

with open("google_leti_test.json", "w", encoding="utf-8") as dat:
  json.dump(results, dat, ensure_ascii=False, indent=2)

for letalisce in letalisca:
    params = {
        "engine": "google_flights",
        "departure_id": letalisce,
        "arrival_id": destinacija,
        "outbound_date": odhod_datum,
        "return_date": prihod_datum, 
        "currency": "EUR",
        "hl": "sl",
        "api_key": key
    }
    search = GoogleSearch(params)
    novi_podatki = search.get_json()
    
    with open("google_leti_test.json", "r") as dat:
        content = dat.read().strip()
        obstojeci_podatki = json.loads(content) if content else {}
        obstojeci_podatki.update(novi_podatki)
    
    with open("google_leti_test.json", "w") as dat:
        json.dump(obstojeci_podatki, dat, ensure_ascii=False, indent=2)

with open("google_leti_test.json", "r") as dat:
    content = json.load(dat)
    print(content["best_flights"])
    