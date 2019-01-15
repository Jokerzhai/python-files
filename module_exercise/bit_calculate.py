"""
按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：
下表中变量 a 为 60，b 为 13，二进制格式如下：
"""
a = 60      #60 = 0011 1100
b = 13      #13 = 0000 1101
c = 0

c = a & b;
print "a&b 的值为： ", c

c = a | b;
print "a|b 的值为： ", c

c = a ^ b;
print "a^b 的值为： ", c

c = ~a;
print "~a 的值为： ", c

c = ~b;
print "~b 的值为： ", c

c = a << 2;
print "a<<2 的值为： ", c

c = a >> 2;
print "a>>2 的值为： ", c