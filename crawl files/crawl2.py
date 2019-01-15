#-*- coding:utf - 8 -*-
#实现一个简单的爬虫，爬取百度贴吧图片
import urllib2 #python内置的HTTP请求库
import re

#根据url获取网页html内容
def getHtmlContent(url): 
    page = urllib.urlopen(url)
    return page.read()#response对象有一个read方法，可以返回获取到的网页内容
#urlopen 一般常用的有三个参数，它的参数如下：
#urllib.request.urlopen(url,data,timeout)
#url得到的是网页的内容 即网页的源码 HTML框架
#data 是访问URL时要传送的数据
#timeout 是设置超时时间
#data和timeout是可以不传送，为默认值


#从html中解析出所有图片的url
#百度贴吧html中jpg图片的url格式为：<img ... src= "XXX.jpg" width = ...>
def getJPGs(html):
    #解析jpg图片的正则
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width')
    #注：这里最后加一个'width'是为了提高匹配精确度
    jpgs = re.findall(jpgReg,html)
    return jpgs

#用图片url下载图片并保存成指定文件名
def downloadJPG(imgUrl,fileName):
    urllib.urlretrieve(imgUrl,fileName)

#批量下载图片，默认保存到当前目录下
def batchDownloadJPGs(imgUrls,path = './'):
    #用于给图片命名
    count = 1
    for url in imgUrls:
        downloadJPG(url,''.join([path,'{0}.jpg'.format(count)]))
        count +=1

#封装:从百度贴吧网页下载图片
def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)

def main():
    url = 'http://tieba.baidu.com/p/2256306796'
    download(url)

if __name__ == '__main__':
    main()
