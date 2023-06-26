#most common applications in Python: Histograms
#When we encounter a new name, we add a new entry
#in the dictionary; if ii's the second or later time
#we add the occurrence:

counts = dict()
names = ['paul', 'Ole', 'paul', 'rick', 'paul']
for name in names :
    if name not in counts:
        counts[name] = 1
        print(counts)
    else :
        counts[name] = counts[name] + 1
        print(counts)
print(counts)
