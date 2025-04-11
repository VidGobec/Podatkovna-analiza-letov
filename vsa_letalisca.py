import requests
import json

key = "dac4581eb8885686f5477fb21606b6e8"

offset = 0
total = 1
data = []
while offset < total:
    url = f"https://api.aviationstack.com/v1/airports?access_key={key}&offset={offset}"
    response = requests.get(url).json()
    offset = response["pagination"]["offset"]
    total = response["pagination"]["total"]
    offset += 100

    data = data + response["data"]


with open(f"vsa_letalisca.json", "w") as dat:
    json.dump(data, dat)