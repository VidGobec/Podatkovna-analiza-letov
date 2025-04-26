import json, requests, time
from podprogrami import iata
from podprogrami.izbiralec_letov import IzbiralecLetov
from serpapi import GoogleSearch
key = "30aaff7063797c81850350cf7d1f86969cc9952fd844c9d917d5b0f4eef0907f"
params = {
                "type" : 1,
                "engine": "google_flights",
                "departure_id": "LJU,ZAG,TRS,TSF,RJK",
                "arrival_id": "SIN",
                "outbound_date": "2025-05-05",
                "currency": "EUR",
                "hl": "sl",
                "api_key": key
            } 
params["return_date"] = "2025-05-08"
search = GoogleSearch(params)
results = search.get_json()
print(results)