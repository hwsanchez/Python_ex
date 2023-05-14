#while vs for loop
# A definite loop using a for statement is much more elegant
# the iteration variable is completely taken care of by the for loop
# len() function returns the lenght of a string


fruit = 'banana'
index = 0
while index < len(fruit):
    print(fruit[index])
    index = index +1

count = 0
for letter in fruit :
    print(letter)
    if letter == 'a' :
        count = count + 1
print('there are this amount of a in Banana:', count)
