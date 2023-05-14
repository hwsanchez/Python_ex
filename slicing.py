#String Slicing:
s = "Monty Python"
print(s[0:4])   #print s sub 0 through (but NOT including 4) = Mont
print(s[6:7])   #prints P
print(s[6:20])  #prints Python

#Yo can eliminate the first or last digit inside the brackets:
#If the first one is ommited , it assumes the beginning of the String
#If the last one is ommited, it assumes the end of the String

name = "Hugo Sanchez"
print(name[ :4])
print(name[5: ])
print([ : ])
