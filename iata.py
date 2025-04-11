import requests

def iata(iata):
    """Funkcija vrne pove če obstaja IATA koda.
    """
    url = "https://raw.githubusercontent.com/jbrooksuk/JSON-Airports/refs/heads/master/airports.json" #https://github.com/jbrooksuk/JSON-Airports
    res = requests.get(url)
    data = res.json()
    return iata in [letalisce["iata"] for letalisce in data]

evropa_iata = ["DEN", "CAN", "HKG", "CTU", "SZX", "CKG", "MIA", "PHX", "SEA", "LAS"]

for letalisce in evropa_iata:
    print(iata(letalisce))