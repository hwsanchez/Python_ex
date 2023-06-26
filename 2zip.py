#using zip to compare 2 or more lists:

x = [1,2,3,4]
y = [1,1,3,7,9]

for i, j in zip(x,y):
    if i == j:
        print('Same')
    else:
        print('Not same!')

#zip
