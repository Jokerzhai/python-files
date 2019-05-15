
import re

import requests

import os

from urlparse import urlsplit

from os.path import basename

headers = {

'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",

'Accept-Encoding': 'gzip, deflate'}

def mkdir(path):

if not os.path.exists(path):

print '�½��ļ���:', path

os.makedirs(path)

return True

else:

print u"ͼƬ�����:", os.getcwd() + os.sep + path

return False

def download_pic(img_lists, dir_name):

print "һ���� {num} ����Ƭ".format(num=len(img_lists))

for image_url in img_lists:

response = requests.get(image_url, stream=True)

if response.status_code == 200:

image = response.content

else:

continue

file_name = dir_name + os.sep + basename(urlsplit(image_url)[2])

try:

with open(file_name, "wb") as picture:

picture.write(image)

except IOError:

print("IO Error\n")

continue

finally:

picture.close

print "���� {pic_name} ���!".format(pic_name=file_name)

def get_image_url(qid, headers):

# �����������ʽ��Դ�����е�ͼƬ��ַ���˳���

#reg = r'data-actualsrc="(.*?)">'

tmp_url = "https://www.zhihu.com/node/QuestionAnswerListV2"

size = 10

image_urls = []

session = requests.Session()

while True:

postdata = {'method': 'next', 'params': '{"url_token":' +

str(qid) + ',"pagesize": "10",' + '"offset":' + str(size) + "}"}

page = session.post(tmp_url, headers=headers, data=postdata)

ret = eval(page.text)

answers = ret['msg']

print u"���� : %d " % (len(answers))

size += 10

if not answers:

print "ͼƬURL��ȡ���, ҳ��: ", (size - 10) / 10

return image_urls

#reg = r'https://pic\d.zhimg.com/[a-fA-F0-9]{5,32}_\w+.jpg'

imgreg = re.compile('data-original="(.*?)"', re.S)

for answer in answers:

tmp_list = []

url_items = re.findall(imgreg, answer)

for item in url_items: # ����ȥ���õ���ͼƬURL�е�ת���ַ�'\\'

image_url = item.replace("\\", "")

tmp_list.append(image_url)

# ������ͷ���ȥ�� ��ȡdata-original������

tmp_list = list(set(tmp_list)) # ȥ��

for item in tmp_list:

if item.endswith('r.jpg'):

print item

image_urls.append(item)

print 'size: %d, num : %d' % (size, len(image_urls))

if __name__ == '__main__':

#question_id = 26037846

question_id =34078228

zhihu_url = "https://www.zhihu.com/question/{qid}".format(qid=question_id)

path = 'zhihu_pic'

mkdir(path) # ���������ļ���

img_list = get_image_url(question_id, headers) # ��ȡͼƬ�ĵ�ַ�б�

download_pic(img_list, path) # ����ͼƬ