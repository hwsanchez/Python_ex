#the .difference method shows which elements from s1 are not present in s2:


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

s4 = s1.difference(s2)
print(s4)

# result: {1}

#which elelments from s2 are not in s1?
s5 = s2.difference(s1)
print(s5)

#difference with multiple sets
#which values from s3 are NOT in s2 AND s1?

s6 = s3.difference(s1, s2)
print(s6)
#result: {5}
