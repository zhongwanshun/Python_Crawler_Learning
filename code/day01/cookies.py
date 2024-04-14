import requests

url = "http://download.java1234.com/user/login"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
data = {
    'userName': 'python222',
    'password': '123456'
}
r = requests.post(url=url, data=data, headers=headers)
print(r.text)
print(r.headers)
cookieJar = r.cookies
for c in cookieJar:
    print(c.name, c.value)
    targetUrl = "http://download.java1234.com/user/userDownload/list/1"
    r2 = requests.get(url=targetUrl, headers=headers, cookies=cookieJar)
print(r2.text)
