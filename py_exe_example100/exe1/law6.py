#title:有四个数字：1、2、3、4 ，能组成多少个互不相同且无重复数字的三位数？各是多少
#analysis：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列
#为了减少冗余判断和循环，可以做优化
for i in range (1,5):
    for j in range(1,5):
        if (j==i):
            continue;
            for k in range(1,5):
                if (k == i or k == j):
                    continue;
                print(i,j,k);