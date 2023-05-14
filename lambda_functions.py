#Experimenting with Lamba functions
#Here is a simple fnction that doubles a number
def double(n):
    return n*2
x = input('Enter a number: ')
print('Function result: The double is', double(int(x)))

#now the same with a lambda function: you create a variable and assign it a lambda function which contains an argument the : sign and a return calculation(single line code)

double = lambda n:n*2
x = input('Enter a number: ')
print('Lambda function result: The double is', double(int(x)))
