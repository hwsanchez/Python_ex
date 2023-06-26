#Here we remove duplicates from a list using sets:

l1 = [1, 2, 3, 1, 2, 3, 4]
l2 = set(l1)
print(l2)
#cool, but its a set and not a list.
#instead do this:
l3 = list(set(l1))
print(l3)
