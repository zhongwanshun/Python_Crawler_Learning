import requests

url = "https://www.baidu.com/s?"

data = {
    "wd": "宝马"
}

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

}

r = requests.get(url=url, params=data, headers=header)

r.encoding = "utf-8"

print(r.status_code)
print(r.url)
print(r.text)
