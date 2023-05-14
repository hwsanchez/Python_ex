#Parsing and extracting:
data = 'From hwsanchez.poreda@gmail.com Sat Jun 3 2004'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)
