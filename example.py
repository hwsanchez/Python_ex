#bunch of lists:
employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane' ]

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

#Which members are developers and go to the gym?


result = set(gym_members).intersection(developers)
print(result)

#notice we have to wrap gym_members in a set() function because .inersection() only works for sets.

#Which employees are NOT developers OR Gym members?

result = set(employees).difference(gym_members, developers)
print(result)

#to search a List takes a lot of computing power, to search a set is more efficient

#List membership test:
if 'Corey' in developers:
    print('Corey is a developer!')

#same membership test with a set (faster!!)

s = set(employees)
if 'Steven' in developers:
    print('Steven is a developer!')
