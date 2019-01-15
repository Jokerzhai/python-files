## for iterating_var in sequence:
#    statements(s)
# python 的 for 循环更智能

for letter in 'Python':     #第一个实例
    print '当前字母 ：',letter

fruits = ['bannna','apple','mange']
for fruit in fruits:        #第二个实例
    print '当前水果 ：', fruit

print "Good bye!"

##第二种方法实现实例二
#  函数len()返回列表的长度，即元素的个数。range返回一个序列的数
# 但是fruits[index]，就是返回fruits[0]、fruits[1]、fruits[2]
fruits = ['banana','apple','mango']
for index in range(len(fruits)):
    print '当前水果 ：', fruits[index]

print "Good bye!"
"""
#循环中使用else语句
#在python中，else中的语句会在循环正常执行完（for不是通过break跳出而中断的）的情况下执行
for num in range(10,20):      #迭代10到20之间的数字
    for i in range(2,num)：   #根据因子迭代
        if num%i == 0:        #确定第一个因子
            j = num/i        #计算第二个因子
            print '%d 等于 %d * %d' % (num,i,j)
            break           #跳出当前循环
    else:                   #循环的else部分
        print num, '是一个质数'
"""
#使用循环画等腰直角三角形
rows = int(raw_input('输入列数：    '))
i = j = k = 1 #声明变量，i