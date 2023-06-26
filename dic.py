#Dictionaries are a type of Collection(like Lists)
#A Dictionary is a "bag" of values, each with its own label
#Dictionaries allow us to do fast database-like operations in Python

purse = dict()
purse['money'] = 50
purse['candy'] = 3
purse['keys'] = 5
print(purse)
print(purse['keys'])
purse['candy'] = purse['candy'] + 2
print(purse)

#Dictionary Literals (Constants):

jjj = { 'chuck' : 1 , 'fred' : 42, 'Jan' : 5}
print(jjj)
ooo = {}
print(ooo)
