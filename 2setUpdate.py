#Adding elements to a s
#Add function: .add()

s1 = {1,2,3,4,5}
s1.add(6)
print(s1)

#To add multiple values in a list use .update()

s1.update([6, 7, 7, 8, 9, 9])
print(s1)

#here we add a list plus another set using .update()

s2 = {8, 10, 11, 12, 1}
s1.update(s2, [12, 13, 14])
print(s1)

#result: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
