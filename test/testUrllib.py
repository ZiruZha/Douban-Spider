# -*- coding = utf-8 -*-
# @Time : 2021/6/13 2:34
# @Author : ZIRU ZHA
# @File : testUrllib.py
# @Software : PyCharm


import urllib.request

'''
#  获取一个get请求
response = urllib.request.urlopen("http://www.baidu.com") #  将结果保存在http.client.HTTPResponse对象中

print(response)
print(response.read()) #  读取对象中的信息
print(response.read().decode('utf-8')) #  对获取到的网页源码用utf-8解析，防止中文乱码
'''

#  获取一个post请求
'''
#  报错，使用post方式访问时，需要传递表单信息
response = urllib.request.urlopen("http://httpbin.org/post")
print(response.read())
'''

'''
import urllib.parse
# 用post方式封装数据
# 模拟用户真实登录的时候使用
data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8") #  用data封装数据
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read().decode("utf-8"))
'''

'''
# 超时处理

# response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
# print(response.read().decode("utf-8"))

try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
    print(response.read().decode("utf-8"))
# except urllib.error.URLError: #  教程中的错误类型
#     print("time out")
# import socket
# except socket.timeout: # 引入socket库可以使用socket.timeout类型的错误
#     print("time out")
except OSError: # 也可以使用OSError型的错误，不用新引入库
    print("time out")
# except Exception:
#     print("time out")
'''

'''
response = urllib.request.urlopen("http://www.baidu.com")
#print(response.status)
#print(response.getheaders())
print(response.getheader("Server"))
'''

'''
# 伪装浏览器访问
url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}
data = bytes(urllib.parse.urlencode({"name": "eric"}), encoding="utf-8")
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
respone = urllib.request.urlopen(req)
print(respone.read().decode("utf-8"))
'''

url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}
req = urllib.request.Request(url=url,  headers=headers)
respone = urllib.request.urlopen(req)
print(respone.read().decode("utf-8"))