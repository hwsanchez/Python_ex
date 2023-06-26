#Sort by values instead of keys
#If we could construct a list of tuples of the form (value, key)
#we could sort by values
#We create a data structure that serves our purpose for this:

d = {'b':1, 'c':22, 'a':10}
#temporary list
temp = list()
#we iterate through all items of d
#and append value and key (backwards) # TODO:
#the temporary list

for k, v in d.items():
    temp.append( (v, k) )

print(temp)

#now we apply sort()
print(sorted(temp))
