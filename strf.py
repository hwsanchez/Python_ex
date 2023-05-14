#More String Functions:
greet = 'Hello World!'
print('Original:', greet)
print('original.upper() = ')
print(greet.upper())

#replace():

greeting = ('Hola *!')
nombre = input('type your name: ')
print(greeting.replace('*', nombre))

#Stripping Whitespace:

greet = '  Hello Bob  '
greet.lstrip() #lstrip() removes the spaces to the left
greet.rstrip() #rstrip removes the spaces to the right
greet.strip() #strip() removes spces to the left AND right

#Prefixes:

line = 'Please enter the number: '
line.startwith('Please')
#returns True
