#Muti-conditionals: elif = else if
#Always pay attention to the indentation!
x = input('Type an integer: ')
x = int(x)
if x < 10 :
    print('Small')
elif x < 100 :
    print('Medium')
elif x < 500 :
    print('Large')
elif x < 1000 :
    print('Huge')
else :
    print('Ginormous')
    
