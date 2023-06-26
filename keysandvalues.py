#Retrieving lists of Keys AND values
# this is a dictionary:
mydictionary = {'John' : 56 , 'Jill' : 50 , 'Pauline' : 47}
print(type(mydictionary))
print(mydictionary)

#turning a dictionary into a list
mylist = list(mydictionary)

print(type(mylist))
print(mylist)

#function for printing the keys
print(mydictionary.keys())

#function to print the values:
print(mydictionary.values())

#function for printing the items:
print(mydictionary.items())
