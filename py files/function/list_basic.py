#-*- coding: utf-8 -*-

a = [1,2,3,'z',[4.5,8.9]]

b = a[3]            #返回一个序列的元素
c = a[1:4]          #返回一个切片
d = a[1:4:2]        #返回一个扩展切片

e = len(a)          #a中的元素数
f = min(a)          #a中的最小值
g = max(a)          #a中的最大值
h = all(a)          #检查a中的所有项是否为True
i = any(a)          #检查a中的任意项是否为True
print b, c, d, e, f, g, h, i