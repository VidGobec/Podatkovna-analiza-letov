
url = "https://serpapi.com/search.json?engine=google_flights&departure_id=CDG&arrival_id=AUS&outbound_date=2025-04-11&return_date=2025-04-17&currency=EUR&hl=en"
key = "9aa8f07a4838c4c78081cbafe35b26cd7389b628269b05fe8304a3e55f902c47"

import json
import matplotlib.pyplot as plt
import random
import requests



from serpapi import GoogleSearch

params = {
  "type" : 2,
  "engine": "google_flights",
  "departure_id": "LJU",
  "arrival_id": "SIN",
  "outbound_date": "2025-07-15",
  "currency": "EUR",
  "hl": "en",
  "api_key": key
}

search = GoogleSearch(params)
results = search.get_json()


with open(f"googleleti.json", "w") as dat:
  json.dump(results,dat, ensure_ascii=False, indent=2)


