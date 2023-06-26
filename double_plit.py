#Double split pattern:
line = 'From stephen.miller@uct.ac.az Sat Jan 5 09:14:16 2022'
print(line)
words = line.split()
print(words)
email = words[1]
print(email)
#This split separates the email from the server address
parts = email.split('@')
print(parts)
