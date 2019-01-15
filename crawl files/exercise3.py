#-*- coding:utf - 8 -*-
#爬取贴吧图片，网址 ： http://

import urllib.request
import re 
import os

def fetch_pictures(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile()
    


