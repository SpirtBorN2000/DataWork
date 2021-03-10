import json
import requests
url = 'https://api.github.com/users/SpirtBorN2000/repos'
params = {'accept': 'application/vnd.github.v3+json'}
hs = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36', 'Accept':'*/*'}
response = requests.get(url, params=params, headers=hs)
j_body = response.json()

with open('j_body.json', 'w',encoding="utf-8") as write_js:
    json.dump(j_body, write_js)
