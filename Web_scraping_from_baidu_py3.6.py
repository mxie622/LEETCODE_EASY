

import urllib
import requests
import re
import sys, os

cwd=os.getcwd() # Check where your files are stored
print(cwd)
sys.path # Go there to get the images

def getHtml(url):
    html = requests.get(url).text
    urls = re.findall('"objURL":"(.*?)"',html, re.S)
    return urls

def downloadImg(urls):
    x = 1
    for url in urls:
        img = requests.get(url, allow_redirects=False)
        with open(str(x)+'.jpg', 'wb') as f:
            f.write(img.content)
            print('正在下载第%s张图片' % x)
        x+=1
        if x>50:                     #设置爬取图片的张数
            break
    return None

# 李嘉诚的图片
html = getHtml('http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1541120888948_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=李嘉诚')

downloadImg(html)