import koordinate_iata as coord_iata
import requests, json, os

svet_iata = ["JFK", "DXB", "HND", "LHR", "IST", "DEL", "PVG", "LAX", "ICN", "CDG", "SIN", "PEK", "MAD", "AMS", "FRA", "BKK", "KUL", "DOH", "FCO", "YYZ", "GRU", "SGN", "MNL", "MEX", "SYD", "ATL", "BOM", "BOG", "CGK", "JED", "GRU", "DFW", "CAI", "ORD", "SCL", "JNB", "TPE", "AKL"]

#Pridobivanje podatkov 
params = {"access_key": "62905fc234eca138b48941106dcc9e98", 
             "dep_iata": svet_iata}

res = requests.get("https://api.aviationstack.com/v1/flights", params=params)

