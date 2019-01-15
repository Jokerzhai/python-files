print('What is your name ?')
name = raw_input()
print ('What is your age?')
age = raw_input()

if name == 'Alice':
    print('Hi,Alice.')
elif age < 12:
    print('You are not Alice,kiddlo')
elif age > 2000:
    print('error2')
elif age > 100:
    print('error1')