import re
pattern = re.compile(r'\d+')

result1 = re.search(pattern,'abc192def')

if result1:
	print result1.group()
else:
	print 'fail1'