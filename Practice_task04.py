#1. Write a program that repeatedly prompts a user for integer numbers
#until the user enters 'done'. Once 'done' is entered, print out the
#largest and smallest of the numbers. If the user enters anything other
#than a valid number catch it with a try/except and put out an appropriate
#message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


max_number = -1
min_number = None #None is equivalent to Null
while True:
    #try-except tries to do some code and if it blows up then it runs the code in except.
    number = input('Enter a number(type "done" to finish): ')
    try:
        number = int(number)
    except :
        if number == 'done':
            break
        else:
            print('Not a number!')
            continue
    if number > max_number :
        max_number = number
    if min_number is None:
        min_number = number
    elif number < min_number:
        min_number = number
if max_number == -1:
    print('Program ended by user.')
else:
    print('The biggest number you entered is:', max_number)
    print('The smalles number you entered is:', min_number)
