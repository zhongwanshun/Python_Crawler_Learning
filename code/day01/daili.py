import requests

url = "https://cip.cc/"

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

}

proxies = {
    'http': "221.131.165.73:40689"

}

r = requests.get(url=url, proxies=proxies, headers=header)

print(r.status_code)
print(r.url)
# print(r.text)

with open('proxies.html', 'w', encoding='utf-8') as f:
    f.write(r.text)
