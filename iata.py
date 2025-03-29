import requests

def iata(iata):
    """Funkcija vrne pove če obstaja IATA koda.
    """
    url = "https://raw.githubusercontent.com/jbrooksuk/JSON-Airports/refs/heads/master/airports.json" #https://github.com/jbrooksuk/JSON-Airports
    res = requests.get(url)
    data = res.json()
    return iata in [letalisce["iata"] for letalisce in data]
