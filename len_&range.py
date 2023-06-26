#Python List:
friends = ['Benni', 'Matthias', 'John', 'Nando']
print('Your friends are:', friends)
#The len() function returns the lenght of the List
print('You have this number of friends:', len(friends))

#The range() function returns a list of numbers, the function takes a number parameter
#and returns a list of numbers from 0 up to, but not including, the parameter number.

for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Year', friend)
print('done')
