#just like Strings, Tuples are UNMUTABLE
#Lists are MUTABLE:

x = [9, 8, 7]
print(x)
x[2] = 6
print(x)

#Assigning another value to a defined Tuple will explode:

##TypeError: 'tuple' object does not support item assignment
#The reason Tuples are not modifyable is EFFICIENCY

#The ONLY Methods available for Tuples are:
#count()
thistuple = (1, 3, 4, 3, 6, 3, 4, 1, 3)
a = thistuple.count(3)
print(a)
#>>> 4

#index()

i = thistuple.index(4)
print(i)
#returns the index of the first item with the parameter value
#>>> 2
