#we want to compare both lists and check which elements are equal
x = [1,2,3,4]
y = [1,1,3,7,9]
for i in range(min(len(x),len(y))):
    if x[i] == y[i]:
        print('Same')
    else:
        print('Not same')
# for i in range(min(len(x),len(y))):
#     if x[i] == y[i]:
#         print('Same')
#     else:
#         print('Not same!')


#The zip() function:
 # zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.
 # |
 # |     >>> list(zip('abcdefg', range(3), range(4)))
 # |     [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
 # |
 # |  The zip object yields n-length tuples, where n is the number of iterables
 # |  passed as positional arguments to zip().  The i-th element in every tuple
 # |  comes from the i-th iterable argument to zip().  This continues until the
 # |  shortest argument is exhausted.
 # |
 # |  If strict is true and one of the arguments is exhausted before the others,
 # |  raise a ValueError.

print(list(zip(x,y)))

#result:
#[(1, 1), (2, 1), (3, 3), (4, 7)]

z = ['one', 'two', 'three']

print(list(zip(x,y,z)))

#result:
#[(1, 1, 'one'), (2, 1, 'two'), (3, 3, 'three')]
