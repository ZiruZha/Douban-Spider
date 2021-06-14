# -*- coding = utf-8 -*-
# @Time : 2021/6/13 19:32
# @Author : ZIRU ZHA
# @File : testBs4.py
# @Software : PyCharm

'''
# BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为四种

-Tag
-NavigableString
-BeautifulSoup
-Comment

'''
import re

from bs4 import BeautifulSoup

file = open("./百度一下，你就知道.html", "rb")
# html = file.read()
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(type(bs.head))

# 1.Tag 标签及其内容：获得找到的第一个内容

# print(bs.title.string)
# print(type(bs.title.string))

# 2.NavigableString 标签里的内容——字符串

# print(bs.a.attrs)
# sttrs 获取标签的所有属性，返回一个字典


# print(type(bs))
# 3.BeautifulSoup 表示整个文档

# print(bs.a.string)
# print(type(bs.a.string))

# 4.Comment是一个特殊的NavigableString，输出的内容不包含注释符号


# ------------------------------------
# 应用
# 文档的遍历
# print(bs.head.contents)
# 搜索beautiful soup遍历文件树获取全部

# 文档的搜索

# 1.find_all()
# 字符串过滤：查找与字符串完全匹配的内容
# t_list = bs.find_all("a")

# 正则表达式搜索：使用search()方法匹配内容
# t_list = bs.find_all(re.compile("a"))

# 方法：传入一个函数根据函数的要求搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")  # 标签中含有”name“
#
#
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)


'''
# 2.kwargs  参数
t_list = bs.find_all(id="head")
t_list = bs.find_all(class_=True)
for item in t_list:
    print(item)
'''
'''
# 3.text文本参数
# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123", "地图", "贴吧"])
t_list = bs.find_all(text=re.compile("/d"))  #  应用正则表达式来查找包含特定文本的内容（标签里的字符串）
'''
'''
# 4.limit参数
t_list = bs.find_all("a", limit=3) #限定个数
'''

# css选择器
# t_list = bs.select('title')  # 通过标签查找
# t_list = bs.select(".mnav")  # 通过类名查找
# t_list = bs.select("#u1")  # 通过id查找
# t_list = bs.select("a[class = 'bri']")  # 通过属性查找
t_list = bs.select("head > title")  # 通过子标签查找
for item in t_list:
    print(item)
