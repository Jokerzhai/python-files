#This program says hello and asks for my name
print('Hello world!')
print('What is your name?')
myName = raw_input()    #Python3 is input() while Python2 is raw_input()
print('It is good to meet you, ' + myName)
print('The length of your name is :  ')
print(len(myName))
print('What is your age?')
myAge = raw_input()
print('You will be '+str(int(myAge)+1)+'in a year.')