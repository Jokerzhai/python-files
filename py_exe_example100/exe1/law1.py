"""
title:有四个数字：1、2、3、4 ，能组成多少个互不相同且无重复数字的三位数？各是多少
analysis：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列
function: range(start,stop[,step])
parameter1 analysis:start:计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
parameter2 analysis:stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
parameter3 analysis:step:step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1) 
"""
l = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != k) and (i != j) and (j !=k):
                l.append([i,j,k])
print "总数量： ", len(l)
print l
#raw_input("按下enter键退出，其他任意键显示...\n")