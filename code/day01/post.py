import json

import requests

url = "https://fanyi.baidu.com/sug"

query = {
    "kw": "apple"
}

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

}

p = requests.post(url=url, params=query, headers=header)

print(p.status_code)
# print(p.text)
j = json.loads(p.text)

print(j)
