from serpapi import search

params = {
    "q": "coffee",
    "location": "Austin, Texas, United States",
    "api_key": "your_api_key"
}

results = search.GoogleSearch(params).get_dict()
print(results)