import koordinate_iata as coord_iata
import requests, json, os

evropa_iata = ["LHR", "IST", "CDG", "AMS", "MAD", "FRA", "BCN", "FCO", "LGW", "SVO", "MUC", "LIS", "DUB", "ATH", "VIE", "ZRH", "MXP", "OSL", "BRU", "WAW", "BUD", "ARN", "VCE", "NCE", "OTP", "HEL", "BEG", "KEF"]

# Shranjevanje
#Pridobivanje podatkov 
params = {"access_key": "62905fc234eca138b48941106dcc9e98", 
             "dep_iata": evropa_iata}

res = requests.get("https://api.aviationstack.com/v1/flights", params=params)

print(res.json())