#list def in Python:
A = [1,2,3,4,5,6,7,8]
print(A)

#makes a range from 0 to 10, but not including 10
print(range(10))

#makes a list with elements from 0 to 10 but not including 10:

B = list(range(10))
print(B)

#prints the type of element at index 0 in the B list (Integer)
print(type(B[0]))

#turning all elements in B into a list of strings:
C = [str(erbicho) for erbicho in B]
print(C)

#akward list:

X = ['tralala', 2, 3.4, False, True, 'Hahahahaha!']
print([type(lavaina) for lavaina in X])
