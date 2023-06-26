#The get method for dictionaries:

counts = dict()
names = ['paul', 'Ole', 'paul', 'rick', 'paul']
for name in names :
    counts[name] = counts.get(name, 0) + 1
    print(counts)
print(counts)
