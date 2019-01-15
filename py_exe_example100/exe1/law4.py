#title:有四个数字：1、2、3、4 ，能组成多少个互不相同且无重复数字的三位数？各是多少
#analysis：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列
#python自带函数
from itertools import permutations
for i in permutations([1,2,3,4],3):
    print(i)