#Tuples and Dictionaries
#The items() method in dictionaries returns a list of (key, value) Tuples

d = dict()
d['minion1'] = 'Kothann'
d['minion2'] = 'Pippppi'
d['minion3'] = 'Rikiti'
d['minion4'] = 'Trikifli Boldis'
#k is key v is value
for (k, v) in d.items():
    print(k, v)
tups = d.items()
print(tups)
