#For loop example. Here we find the largest number in the given array.
numbers = [ 2, 23, 5, 89, 7, 100, 6, 345, 0]
largest = -1
print('The numbers in your array are:')
for number in numbers:
    print(number)
    if number > largest:
        largest = number
print('The largest number in your array is:', largest)
