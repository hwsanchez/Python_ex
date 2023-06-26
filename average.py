#Here are 2 ways to compute averages:
#Traditional way:

suma = 0
count = 0
while True :
    inp = input('1) Enter a number (type done to end): ')
    if inp == 'done'  :
        break
    count = count + 1
    suma = suma + float(inp)
average = suma / count
print('Average:', average)


#same thing but with Lists:
#NOT WORKING AND DONT KNOW WHY!!!!
numlist = list()
while True :
    inp = input('2) Enter a number (type done to end): ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
newAverage = sum(numlist) / len(numlist)
print('Average:', newAverage)
