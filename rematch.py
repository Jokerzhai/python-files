import re
pattern = re.compile(r'\d+')

result1 = re.match(pattern,'192abc')

if result1:
	print result1.group()
else:
	print 'matching fail1'

result2 = re.match(pattern,'abc192')

if result2:
	print result2.group()
else:
	print 'matching fail2'