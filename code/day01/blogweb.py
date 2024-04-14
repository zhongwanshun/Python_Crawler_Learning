import requests

url = "https://www.cnblogs.com/"

blogweb = requests.get(url=url)

print(blogweb.status_code)
# print(blogweb.text)

with open("blogweb.html", "w", encoding="utf-8") as f:
    f.write(blogweb.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(blogweb.text, "lxml", exclude_encodings="utf-8")
article_list = soup.select("article.post-item")
num = 1
for article in article_list:
    print(num)
    title = article.find("a", class_="post-item-title")
    print(title.get_text().strip())
    title_link = article.find("a", class_="post-item-title")
    print(title_link.attrs["href"])
    author = article.find("a", class_="post-item-author")
    print(author.get_text().strip())
    times = article.find("span", class_="post-meta-item")
    print(times.get_text().strip())
    num += 1
    print("----------------------------")
