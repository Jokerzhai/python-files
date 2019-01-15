#-*- coding:utf - 8 -*-
##使用python 爬取豆瓣TOP250电影的评分、评价人数、短评等信息，并在其保存在txt文件中
##资源来源于网络
import requests
from bs4 import BeautifulSoup
import re 
import time 
import sys
import io

def getHTMLText(url,k):
    try:
        if(k==0):kw={}
        else:kw = {'start':k,'filter':''}
        r = requests.get(url,params-kw, headers = {'User-Agent':'Mozilla/4.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Failed")

def getData(html):
    soup = BeautifulSoup(html,"html.parser")
    movieList = soup.find('ol',attrs={'class':'grid_view'})
    #找到第一个class属性值为grid_view的ol标签
    moveInfo = []
    for movieLi in movieList.find_all('li'): #找到所有li标签
        data = [] #得到电影名字
        movieHd = movieLi.find('div',attrs={'class':'hd'})
        #找到第一个class属性值为hd的div标签
        movieName = movieHd.find('span',attrs={'class':'title'}).getText()
    #找到第一个class属性值为Title的span标签 也可以使用.string方法
    data.append(movieName)

    #得到电影的评分
    movieScore = movieLi.find('span',attrs={'class':'rating_num'}).getText()
    data.append(movieScore)

    #得到电影的短评
    movieQuote = movieLi.find('span',attrs={'class':'inq'})
    if(movieQuote):
        data.append(movieQuote.getText())
    else:
        data.append("无")

    print(outputMode.format(data[0],data[1],data[2],data[3],chr(128)))

#将输出重定向到txt文件
output = sys.stdout
outputfile=io.open("moviedata.txt",'w',encoding='utf-8')
sys.stout = outputfile

outputMode = "{0:{4}^20}\t{1:^10}\t{2:^10}\t{3:{4}<10}"
print(outputMode.format('电影名称', '评分', '评论人数', '短评', chr(128)))
basicUrl = 'https://movie.douban.com/top250'
k = 0
while k <= 225:
    html = getHTMLText(basicUrl,k)
    time.sleep(2)
    k+=25
    getData(html)

outputfile.close()
sys.stdout = output    

