# -*- coding:utf-8 -*-
"""
    爬取python贴吧网页
"""

# 引入需要的模块
import urllib2

# python吧第一页的url地址
url = "http://tieba.baidu.com/f?kw=download_file&ie=utf-8&pn=0 "

# 获取
response = urllib2.urlopen(url)

# 将获取到的内容赋值给content变量
content = response.read()
print content

with open("python_1.html", "w") as f:
    f.write(content)
