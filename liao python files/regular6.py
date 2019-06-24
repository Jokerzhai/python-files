#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 geoogle 456')
result2 = pattern.findall('run8888oob123google456',0,14)

print(result1)
print(result2)


