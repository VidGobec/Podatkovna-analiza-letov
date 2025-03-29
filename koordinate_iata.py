import requests

def koordinate_iata(iata):
    """Funkcija vrne nabor (lon, lat) za koordinate izbranega letališča (iata).
    """
    url = "https://raw.githubusercontent.com/jbrooksuk/JSON-Airports/refs/heads/master/airports.json" #https://github.com/jbrooksuk/JSON-Airports
    res = requests.get(url)
    data = res.json()
    return next(((float(letalisce["lon"]), float(letalisce["lat"])) for letalisce in data if letalisce['iata'] == iata), "Ne obstaja!")

found = any(entry.get("iata") == "LJU" for entry in data)

print("LJU exists" if found else "LJU does not exist")