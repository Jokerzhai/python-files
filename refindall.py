#正则表达式匹配字母
import re
pattern = re.compile(r'\d+')
print re.findall(pattern,'A1B2C3D4')