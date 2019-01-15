import re
pattern = re.compile(r'\d+')

matchiter = re.finditer(pattern,'A1B2C3D4')

for match in matchiter:
	print match.group()