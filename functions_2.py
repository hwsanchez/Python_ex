#Regular function in Python:
def triple(n):
    return n*3

number = input('Type a number: ')
print('(Reg Function) The triple is: ', triple(int(number)))

triple = lambda n:n*3
number = input('Type a number: ')
print('(Lambda Function) The triple is: ', triple(int(number)))

#The Lambda function is also known as an annonymous function since it doen't have any name
#Lambda functions can have multiple parameters separated by commas but only one expression
