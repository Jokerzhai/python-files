import random

def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

def helloName(name):
    print('Hello ' + name)

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain '
    elif answerNumber == 2:
        return 'It is decidedly so '
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'No,you are wrong! '
    elif answerNumber == 5:
        return 'I am so sorry to hear that'
    elif answerNumber == 6:
        return 'Do not worry that'
    elif answerNumber == 7:
        return 'Everything will be fine'
    elif answerNumber == 8:
        return 'Best wishes to you'
    elif answerNumber == 9:
        return 'Blessing for you '


hello()
hello()
hello()

helloName('Joker')
helloName('Lina')

#r = random.randint(1,9)
#fortune = getAnswer(r)
#print(fortune)
print(getAnswer(random.randint(1,9)))