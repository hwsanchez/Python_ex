#Conditional if, if else
#Pay attention to the indentation!

x = 5
if x == 5 :
    print('x is equal (==) to 5')
if x < 10 :
    print('x is less (<) than 10')
if x != 8 :
    print('x is NOT (!=) 8!')
print('Done with conditional if examples')

x = input('x: ')
if int(x) > 30 :
    print('x is greater than (>) 30 ')
elif int(x) == 30 :
    print('x equals (==) 30')
else :
    print('x is less than (<) 30')
print('Done!')
