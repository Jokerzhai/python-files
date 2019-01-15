#title:有四个数字：1、2、3、4 ，能组成多少个互不相同且无重复数字的三位数？各是多少
#analysis：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列
#使用 itertools模块
import itertools

DataIn = list('1234')
TmpList = []
for x in list(itertools.combinations(DataIn,3)):
    TmpList = TmpList + list(itertools.permutations(x,3))
for i in TmpList:
    print(''.join(i))

