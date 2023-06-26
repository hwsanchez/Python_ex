#To remove an item from a set use: .remove(item)

s1 = {1, 2, 3, 4, 5, 6}
s1.remove(4)
print(s1)

#add it again!
s1.add(4)

#if you try to remove something that does not exist on the list, then you'll get an error!

# s1.remove(7)


#we better use the .discard() function which wont return an error if the element doesnt exists:

s1.discard(11)
