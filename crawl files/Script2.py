import urllib
import re

def get_html(url):
    page = urllib.urlopen(url)
    html_code = page.read()
    return html_code

def get_image(html_code):
    reg = r'src="(.+?\.jpg)"width'
    reg_img = re.compile(reg)
    img_list = reg_img.findall(html_code)
    x = 0
    for img in img_list:
        urllib.urlretrieve(img, '%s.jpg' % x)
        x += 1
 

print u "------------网页图片抓取----------"
print u "请输入url: ",
url = raw_input()
if url:
    pass
else:
    print u"-----没有地址输入正在使用默认地址------"
    url = "https://www.zhihu.com/node/QuestionAnswerListV2"
print u "------------正在获取网页----------"
html_code = get_html(url)
print u "-----------正在下载图片-----------"
get_image(html_code)
print u "------下载成功----"
raw_input(' Press Enter to exit')