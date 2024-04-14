from bs4 import BeautifulSoup

# 默认打开的文件编码是gbk，我们需要设置编码
soup = BeautifulSoup(open('test.html', encoding='utf-8'), 'lxml')
# 根据标签名查找DOM节点 找到是第一个符合条件的DOM节点
# DOM DOM值 DOM标签名
print(type(soup.a), soup.a, soup.a.name)
# 获取标题的属性和属性值
print(type(soup.a.attrs), soup.a.attrs['href'])
# 获取标签内容
print(soup.p.string)
# bs4的一些常用方法

# 查找第一个符合条件的元素，支持属性条件
print(soup.find('a'))
print(soup.find('a', target="_blank"))
# class属性特殊点 关键字，所以加个下划线
print(soup.find('a', class_="c2"))
# find_all 返回一个列表
print(soup.find_all('a'))
print(soup.find_all(['a', 'p']))  # 获取多个DOM
print(soup.find_all('li', limit=2))
# select方法,使用 选择器查找元素 返回一个列表
print(soup.select('a'))  # 根据标签选择器
print(soup.select('.c2'))  # 根据类选择器
print(soup.select('#l2'))  # 根据id选择器
# 属性选择器
print(soup.select('li[id]'))  # 查找li标签中有id的DOM
print(soup.select('li[id="l3"]'))  # 查找li标签中id=l3的DOM
# 层级选择器
print(soup.select('div li'))  # 后代选择器 包括儿子和孙子等后代 多个标签名之间用空格
print(soup.select('div > ul > li'))  # 子代选择器 仅限儿子这代 多个标签名之间用 >
print(soup.select('li,p'))
# 获取节点信息
obj = soup.select('#d1')[0]
# 如果标签对象中，只有内容，那么string,get_text()都可以使用
# 如果标签对象中，除了内容还有标签，那么string就获取不到数据 而get_text()是可以获取数据
print(obj.string)
print(obj.get_text().strip())
# 节点属性获取
obj = soup.select('#p1')[0]
print(obj.name)  # 获取标签名
print(obj.attrs)  # 返回属性 字典类型
print(obj.attrs['id'])  # 获取属性值
print(obj['id'])  # 简写
print(obj.attrs.get("class")[0])  # 获取属性值
print(obj.get("class")[0])  # 简写
