#finding the smallest value in an Array using the none type (like null)
#Note the 'is' operator. 'is' demands equality in the type of the values and the value of them. Similar but stronger than ==
#The opposite is 'is not'. use them with Boolean expressions
smallest = None
print('Array:')
for value in [3, 6, 2, 56, 34, 63, 2, 1]:
    print(value)
    if smallest is None:
        smallest = value
    elif value < smallest :
        smallest = value
print('The smallest value is:', smallest)
