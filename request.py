import requests
import json
from enum import Enum

from evropa import evropa_iata

class endpoint(Enum):
    FLIGHTS = "flights"
    AIRPORTS = "airports"
    AIRLINES = "airlines"
    AIRPLANES = "airplanes"
    AIRCRAFT_TYPES = "aircraft_types"
    TAXES = "taxes"
    CITIES = "cities"
    COUNTRIES = "countries"
    #routes ne dela


def get_data(endpoint, sorting = "" ,key = "b6903db5441a48d6449b9543de872baa", params = {}):
    """funkcija prejme string endpoint in kljuc in vrne vse podatke z strani https://api.aviationstack.com/v1/{ENDPOINT}?access_key={KEY}"""
    url = f"https://api.aviationstack.com/v1/{endpoint}?access_key={key}{sorting}"
    return requests.get(url).json()




#data = get_data(endpoint.COUNTRIES.value, "&region=EU")
data = []
with open(f"test.json", "w") as dat:
    for drzava in evropa_iata:
        if len(data) <= 0:
            data = get_data(endpoint.AIRPORTS.value, params={"dep_iata":drzava})
        else:
            data.update(get_data(endpoint.AIRPORTS.value, params={"dep_iata":drzava}))
    json.dump(data, dat)

