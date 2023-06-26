#sets are like lists but dont accept duplicates (it removes them automatically!):
#sets offer some useful methods (get all elemtns that are the same in different sets)
#here we define a set with the function: set()

s1 = set()
print(type(s1))

#here we turn a list of values (inside [] into a set with the set() function:

s2 = set([1, 2, 3, 3, 1, 2, 33])
print(s2)

#notice how sets automathically removes the double values

#if we use curly braces instead of square brackets we define a se:

s3 = {1, 2, 3, 3, 1, 2, 33}
print('s3 is a: ')
print(type(s3))
print(s3)

#for empty sets use the set function:
s4= set()
print('s4= set()', type(s4))

#if you define it like this it will be a dictionary:
s5 ={}
print('s5 ={}', type(s5))
