"""
title:有四个数字：1、2、3、4 ，能组成多少个互不相同且无重复数字的三位数？各是多少
analysis：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列
用集合去除重复元素
这里使用了pprint模块，提供了打印出任何python数据结构类和方法
"""

import pprint

list_num = ['1','2','3','4']
list_result=[]
for i in list_num:
    for j in list_num:
        for k in list_num:
            if len(set(i+j+k))==3:
                list_result+=[int(i+j+k)]
print("能组成%d个互不相同且无重复数字的三位数： "%len(list_result))
pprint.pprint(list_result)
