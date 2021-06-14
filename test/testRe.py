# -*- coding = utf-8 -*-
# @Time : 2021/6/14 15:41
# @Author : ZIRU ZHA
# @File : testRe.py
# @Software : PyCharm

# 正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re
# 创建模式对象
pat = re.compile("AA") #此处的AA是正则表达式，用来去验证其他的字符串
#m = pat.search("ABC")  # search字符串被校验的内容
# m = pat.search("ABCAA")
# m = pat.search("AABCAABAA")# search方法找第一个匹配字符

# # 没有模式对象
# m = re.search("abc", "AabcA") # 前面字符串是规则，后面字符串是被校验的对象
# print(m)

# print(re.findall("a", "abcdabc"))# 前面字符串是规则（正则表达式），后面字符串是被校验的对象

# print(re.findall("[A-Z]", "aAbcdDaBbDc"))
# print(re.findall("[A-Z]+", "aASbcdDFFaBGbDc"))

# sub
# print(re.sub("a", "A", "asdfghasdf")) # 用A替换a

#建议在正则表达式中，被比较的字符串前面加r，不进行转义
a = "aa\taa"
b = r"aa\taa"
print(a,b)

