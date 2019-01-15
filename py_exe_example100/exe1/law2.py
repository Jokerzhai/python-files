#title:有四个数字：1、2、3、4 ，能组成多少个互不相同且无重复数字的三位数？各是多少
#analysis：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列
#改进方法：将for循环和if语句综合成一句，直接打印出结果
list_num = [1,2,3,4]
list = [i*100 + j*10 +k for i in list_num for j in list_num for k in list_num if(j != i and k!=j and k!=i)]
print list