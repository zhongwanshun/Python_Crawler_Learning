import time
from selenium import webdriver

# 创建浏览器操作对象
browser = webdriver.Chrome()
url = "https://www.csdn.net/"
browser.get(url)
time.sleep(5)
content = browser.page_source
print(content)
