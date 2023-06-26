#The intersection function returns all elements that are present in 2 or more sets:

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

s4 = s1.intersection(s2)
print(s4)

#result: {2, 3}

#intersection with 3 sets:

s5 = s1.intersection(s2, s3)
print(s5)

#result: {3}
