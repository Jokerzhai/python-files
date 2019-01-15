#-*- coding:utf - 8 -*-
import urllib2
#import requests

#request = urllib2.Request("http://www.baidu.com")
#response = urllib2.urlopen(request)

response = urllib2.urlopen("http://www.baidu.com")
#调用urllib2库里面的urlopen方法,传入1个URL 
#urlopen 一般常用的有三个参数，它的参数如下：
#urllib.request.urlopen(url,data,timeout)
#url得到的是网页的内容 即网页的源码 HTML框架
#data 是访问URL时要传送的数据
#timeout 是设置超时时间
#data和timeout是可以不传送，为默认值 timeout 默认的是socket._GLOBAL_DEFAULT_TIMEOUT

print response.read()
#response 对象有一个read方法，可以返回获取到网页的内容


