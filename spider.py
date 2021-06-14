# -*- coding = utf-8 -*-
# @Time : 2021/6/12 1:51
# @Author : ZIRU ZHA
# @File : spider.py
# @Software : PyCharm

# 引入库
from bs4 import BeautifulSoup  # 网页解析获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request  # 指定URL，获取网页数据
import urllib.error  # 指定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQlite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    #  1、爬取网页
    datalist = getData(baseurl)
    #  2、解析数据，在第1步中，同步进行
    #  3、保存数据
    savaPath = "豆瓣电影Top250.xls"
    saveData(datalist, savaPath)
    # askURL("https://movie.douban.com/top250?start=")


#  全局变量
#  影片详情链接的正则表达式（规则）
findlink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则（字符串模式）
#  影片图片的链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S  让换行符包含在字符中
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


#  1、爬取网页 + 2、解析数据
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网络源码
        #  2、逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)  #  测试查看电影全部信息
            data = []  # 保存一部电影的全部信息
            item = str(item)

            #  获取影片详情链接
            link = re.findall(findlink, item)[0]  # re库用来通过正则表达式查找指定的字符串
            data.append(link)  # 添加链接

            imgScr = re.findall(findImgSrc, item)[0]
            data.append(imgScr)  # 添加图片

            titles = re.findall(findTitle, item)  # 片名可能只有中文，或同时有中英文
            if (len(titles) == 2):
                chineseTitle = titles[0]  # 添加中文名
                data.append(chineseTitle)
                foreignTitle = titles[1].replace("/", "")  # 去掉无关符号
                data.append(foreignTitle)  # 添加外文名
            else:
                data.append(titles[0])
                data.append(' ')  # 外文名留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)  # 添加评分

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)  # 添加评价人数

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)  # 添加概述
            else:
                data.append(" ")  # 留空

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 替换<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉前后的空格

            datalist.append(data)  # 把处理好的一部电影信息放入datalist

    #print(datalist)
    return datalist


# 得到指定一个URL的网页内容
def askURL(URL):
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 89.0.4389.114 Safari / 537.36"
        # 用户代理
    }
    request = urllib.request.Request(URL, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
        pass
    except OSError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


#  3、保存数据
def saveData(datalist, savePath):
    print("save...")

    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接", "图片链接", "中文名", "外文名", "评分", "评分人数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])  # 数据

    book.save(savePath)  # 保存


if __name__ == "__main__":  # 当程序执行时，整个程序的入口
    # 调用函数
    main()
    print("爬取完毕")
