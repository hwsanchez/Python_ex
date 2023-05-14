#Lambda function with multiple arguments
larger = lambda a,b:a if a > b else b

number1 = input('Enter number 1: ')
number1 = int(number1)
number2 = input('Enter number 2: ')
number2 = int(number2)
print('This number is larger: ', larger(number1, number2))
