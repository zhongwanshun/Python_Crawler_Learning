# 				Python_Crawler_Learning

------

## 一、爬虫

### 1、简介

​	网络爬虫是一种自动化程序，用于在互联网上收集信息。它们模拟人类在网络上浏览的行为，通过访问网页、提取数据和跟踪链接来获取信息。网络爬虫通常由搜索引擎、数据挖掘工程师、研究人员和开发者等使用。

### 2、核心工作

​	网络爬核心工作内容是去目标站点爬取网页，将网页中我们需要的内容进行解析，最后保存，比如保存到Excel，数据库等。

### 3、工作原理

（1）**选择起始点：** 网络爬虫需要一个起始点来开始它的搜索。这可以是一个单个网页、一组网页或整个网站。

（2）**抓取网页：** 爬虫会下载起始点网页的内容，并解析其中的 HTML 或其他标记语言，以识别其中的链接。

（3）**跟踪链接：** 爬虫会分析已下载的网页，提取其中的链接，并添加到待访问的链接列表中。

（4）**访问链接：** 爬虫会按照链接列表中的顺序，逐个访问链接，重复上述步骤，以获取更多的网页内容。

（5）**提取信息：** 爬虫在访问网页时会提取感兴趣的信息，如文本、图片、视频等，并将其存储或进一步处理。

（6）**存储数据：** 爬虫通常会将提取的数据存储在本地数据库或文件中，以备后续分析或展示。

### 4、网络爬虫的应用

​	网络爬虫的应用非常广泛，包括搜索引擎的网页索引、数据挖掘与分析、信息聚合、监测网站变化等。然而，网络爬虫也面临着一些挑战，如处理动态网页、遵守网站的使用条款与隐私政策、防止被反爬虫技术识别等。

### 5、Python的爬虫技术

（1）请求库：`urllib`、`requests`、`selenium`

（2）解析库：`正则`、`xpath`、`jsonpath`、`beautifulsoup`、`pyquery`

（3）存储库：文件、`MySQL`、`Mongodb`、`Redis`

（5）爬虫框架：`Scrapy`

## 二、Request网络请求库

### 1、简介

`requests` 是一个优雅而简洁的 Python HTTP 库，用于发送各种类型的 HTTP 请求。它是 Python 中最受欢迎的 HTTP 客户端库之一，因为它易于使用且功能强大。

### 2、安装

开源地址：https://github.com/psf/requests

中文官方文档：https://requests.readthedocs.io/projects/cn/zh_CN/latest/、

`Win+R`打开输入`cmd`，进入输入（后面的下载地址尽量跟上，要不然会出现下载超时情况）：

```shell
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 3、demo1【**get请求**】

获取百度网页的信息

```Python
# 引入库
import requests
#调用get方法获取网页
r = requests.get("http://www.baidu.com")
# 设置返回对象的编码
r.encoding = "utf-8"
# 返回响应状态码
print(r.status_code)
# 获取网页内容
print(r.text)
# 查看返回对象类型
print(type(r))
```

#### 4、demo2【**get请求**】

实现百度对`Python`这个关键字的查询，并将查询到的页面进行一个反馈:

![image-20240414221457320](images/image-20240414221457320.png)

```python
import requests
url = "https://www.baidu.com/s"
#设置请求头，模拟浏览器正常访问
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
params = {
	'wd': 'Python'
}
r = requests.get(url=url, params=params, headers=headers)
print(r.url)
print(r.status_code)
print(r.text)
```

#### 5、demo03【**post请求**】

在百度翻译输入`orient`发送Get请求，获取搜索的信息

![image-20240414223746220](images/image-20240414223746220.png)

```python
import requests
url = "https://fanyi.baidu.com/mtpe-individual/multimodal?"
#设置请求头，模拟浏览器正常访问
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
query={
    "query"="orient"
}
#post
r = requests.post(url=url, params=data, headers=headers)

print(r.url)

print(r.status_code)
#得到的是unicode编码类型的数据
print(r.text)
#json.loads方法自动把unicode编码转成中文
result = json.loads(r.text)
print(result)
```

## 三、Python反爬

​	很多网站都设置有一定的反爬措施，大量的对数据访问回造成`IP`地址的封禁，为了防止应对反爬虫，我们可以通过设置代理IP。

### 1、代理`IP`简介

​	在网络爬虫、数据采集或访问受限网站时，代理 IP 是常用的工具，它可以帮助隐藏真实 IP 地址并绕过限制，以便顺利获取所需的数据。

### 2、代理IP

匿名程度是：高匿 > 普匿 > 透明。

**1.** **透明代理IP：**顾名思义，服务器知道你在使用代理IP，并且也知道你的真实IP。

**2.** **普匿代理IP：**普匿代理IP要比透明代理IP好一些，但是对方服务器仍然会知道你使用了代理。

**3.** **高匿代理IP：**高匿代理IP不仅可以保护你的IP地址，并且不会改变你的访问请求，让对方服务器毫无察觉，不知道你使用了代理。因此，高匿代理的效果是最好的。

### 3、使用代理IP的基本步骤

(1)**获取代理 IP 地址和端口号**：你可以通过付费或免费的代理服务提供商获取代理 IP 地址和对应的端口号。一些代理服务提供商可能会提供 HTTP、HTTPS 或 SOCKS 代理。

(2)**配置代理参数**：将获取的代理 IP 地址和端口号配置到你的爬虫代码中。

(3)**发送请求时使用代理**：使用 `requests` 或 `urllib` 发送 HTTP 请求时，通过设置代理参数，将请求发送到代理服务器，然后由代理服务器转发请求到目标网站。

### 4、demo4 代理IP使用模板

```python
import requests

# 代理服务器的地址和端口
proxy_host = 'YOUR_PROXY_HOST'
proxy_port = 'YOUR_PROXY_PORT'

# 目标网站
url = 'https://www.example.com'

# 配置代理参数【可以配置多个】
proxies = {
    'http': f'http://{proxy_host}:{proxy_port}',
    'https': f'https://{proxy_host}:{proxy_port}'
}

# 使用代理进行请求
response = requests.get(url, proxies=proxies)

# 处理响应
print(response.text)

```

