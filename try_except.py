#try-except tries to do some code and if it blows up then it runs the code in except.
number = input('Enter a number: ')
try:
    number = int(number)
except :
    number = -1

if number > 0 :
    print('You just typed: ', number)
else :
    print('That is not a number!!')
