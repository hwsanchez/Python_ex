#Strings and Lists
#split function will split each value in between the spaces
#regardless of how many spaces there are and create a List with all elements

name = "John Francis Williams"
print('Full Name:', name)
names = name.split()

lastname = names[2]
print('Last Name:', lastname)
print('Each Name:')
for n in names :
    print(n)

#Split will also split at a designated delimiter:

name = "John;Francis;Williams"
print(name)
names = name.split(';')
print(names)
