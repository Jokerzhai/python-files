import requests
user_agent = 'Mozilla/4.0(compatible; MSIE 5.5;Windows NT)'
headers = {'User-Agent':user_agent}
r = requests.get('http://seputu.com/',headers=headers)
print r.text
soup = BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')
for mulu in soup.find_all(class_="mulu"):