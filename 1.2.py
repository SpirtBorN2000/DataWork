# поменял пару цифр в токене, побаиваюсь выкладывать его на гит, результаты в любом случае есть в json файле
import json
from pprint import pprint
import requests
url = 'https://api.vk.com/method/groups.get'
params = {'access_token':'ba0f18e0fa1f5ca2af61485978241eab4501f2af0dbb54485ef7d07545de731f24a6a0ec65555555','v':'5.130','extended':'1'}
hs = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36', 'Accept':'*/*'}
response = requests.get(url, params=params, headers=hs)
j_bodyvk = response.json()
pprint(j_bodyvk)
with open('j_bodyvk.json', 'w',encoding="utf-8") as write_js:
    json.dump(j_bodyvk, write_js)
