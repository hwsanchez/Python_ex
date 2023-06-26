#>>>help(sorted)
#sorted(iterable, /, *, key=None, reverse=False)
#Return a new list containing all items from the iterable in ascending order.
#iterables are: lists, tuplets, strings, etc...

#tuples are inmutable, but we can order them with sorted()
data = (7, 3, 1, 8, 45, 532, 3, 52)
print(sorted(data))

#the output is a list.
#You can apply sorted() to a string:
print(sorted('Alphabetical'))

#The sort method can sort lists, but it will alter them
#The sorted method is more general, can be applied to iterables (tuplets, lists, strings)
#and the output is a list, meaning the original remains unchanged.
