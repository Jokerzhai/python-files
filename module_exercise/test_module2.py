import re
str1 = 'imooc videonum = 1000'
print str1.find("1000") 
info = re.search(r'\d+',str1)
print info.group()
str2 = 'C++=100,java=90,python=80'
info = re.search(r'\d+',str2)
print info
print info.group()
info = re.findall(r'\d+',str2)
print info
print sum([int(x) for x in info])