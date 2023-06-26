#Sorting Lists of Tuples
#We can take advantage of the ability to sort a list of Tuples to
#get a sorted version of a dictionary

#First we sort the dictionary by the key
#using the items() method AND sorted() function:

d = {'a':10, 'c':22, 'b':1,}
ld = d.items()
print(ld)
print(sorted(ld))
