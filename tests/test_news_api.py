import requests, json
NEWS_API_KEY = "fec27928f08040079d726eb42541c550"


req = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=%s" % NEWS_API_KEY)
req_json = req.json()
#print(req.json())

print(req_json['articles'][3]["title"])
