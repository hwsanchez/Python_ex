#Search using a Boolean value:
array = [2, 4, 5, 7, 8, 12, 14, 24, 34, 43, 35, 67, 77]
convert = lambda n:int(n)
found = False
number = input('Type the number you would like to find in the array:')
number = convert(number)
for value in array:
    if value == number:
        found = True
        break
if found:
    print('The number is in the Array')
else:
    print('The number is not in the Array')
