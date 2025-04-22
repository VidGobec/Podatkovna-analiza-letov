from serpapi import GoogleSearch
import json

letalisca1 = "LJU,KLU,GRZ,/m/04jpl"
letalisca = ["ZAG,TRS,TSF,/m/04jpl", "VCE,TRS,VIE,/m/04jpl", "SZG,LIN,MXP,/m/04jpl", "MUC,STR,FCO,/m/04jpl", "BUD,PRG,ZRH,/m/04jpl"]
destinacija = input("Vpiši IATA kodo kam želiš leteti: ").upper()
datum = input("Vpiši termin (format: YYYY-MM-DD - YYYY-MM-DD): ")

try:
    odhod_datum, prihod_datum = datum.split(" - ")
except ValueError:
    print("Invalid date format. Please use the format YYYY-MM-DD - YYYY-MM-DD.")
    exit()

key = "9aa8f07a4838c4c78081cbafe35b26cd7389b628269b05fe8304a3e55f902c47"

# Rezultati se shranijo tukaj
vsi_rezultati = {}

# Najprej za letalisca1
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
vsi_rezultati[letalisca1] = results.get("best_flights", [])

# Nato za ostala letališča
for letalisce in letalisca:
    params["departure_id"] = letalisce
    search = GoogleSearch(params)
    novi_podatki = search.get_json()
    vsi_rezultati[letalisce] = novi_podatki.get("best_flights", [])

# Shrani v datoteko
with open("google_leti_test.json", "w", encoding="utf-8") as dat:
    json.dump(vsi_rezultati, dat, ensure_ascii=False, indent=2)

# Izpis rezultatov
for depart, flights in vsi_rezultati.items():
    print(f"\nLeti iz {depart}:")
    for flight in flights:
        print(flight)