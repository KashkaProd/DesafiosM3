import requests
import json
url = "https://aves.ninjas.cl/api/birds"

def request_json(url):
    return json.loads(requests.get(url).text)

data = request_json('https://aves.ninjas.cl/api/birds')
#print(data)
