#coding:utf-8
from firstSpider.DataOutput import DataOutput
from firstSpider.HtmlDownloader import HtmlDownloader
from firstSpider.HtmlParser import HtmlParser
from firstSpider.UrlManager import UrlManager
class SpiderMan(object):
	def _init_(self):
		self.manager = UrlManager()
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output = DataOutput()
	def crawl(self,root_url):
		#添加入口URL
		self.manager.add_new_url(root_url)
		#判断url管理器中是否有新的url，同时判断抓取了多少个url
		while(self.manager.has_new_url() and self.manager.old_url_size()<100):
			try:
				#从URL管理器获取新的url
				new_url = self.manager.get_new_url()
				#HTML下载器下载网页
				html = self.downloader.download(new_url)
				#HTML解析器抽取网页数据
				new_urls,data = self.parser.parser(new_url,html)
				#将抽取的url添加到URL管理器中
				self.output.store_data(data)
				print "已经抓取%s个链接"%self.manager.old_url_size()
			except Exception,e:
				print "crawl failed"
				#数据存储器将文件输出成指定格式
		self.output.output_html()
		
	if _name_ =="_main_":
		spider_man = SpiderMan()
		spider_man.crawl("http://baike.baidu.com/view/284853.htm")