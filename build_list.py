#Building a list from scratch in Python:
#Constructor form:
stuff = list()
#append method adds items to the list
stuff.append('ice cream')
stuff.append(100)
print(stuff)
stuff.append('Oreos')
print(stuff)

#Python has 2 operators that let you check if an item is in a List
#These are logical operators (return true or false) and do NOT modify the List

print('is Oreos in the list?', 'Oreos' in stuff)
print('is 100 in the list?', 100 in stuff)
print('is R2-D2 in the list?', 'R2-D2' in stuff)

#the in operator can also ask with not

print('is 100 not in the list?', 100 not in stuff)
