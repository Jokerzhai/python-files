import re 
p = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)')  #ʹ����������
s = 'i say , helllo world!'
print p.sub(r'\g<word2> \g<word1>',s)
p = re.cpmpile(r'(\w+)(\w+)')  #ʹ�ñ��
print p.sub(r'\2 \1',s)
def func(m):
	return m.group(1).title() + ''+ m.group(2).title()
print p.sub(func,s)