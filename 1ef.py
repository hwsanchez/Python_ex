#Problem: We want to iterate through a list and get the index and value of EACH element.
#2 old ways of doing it:

# Way 1: looping through the elements of a list w for loop

my_list = ['apples', 'pears', 'mangoes', 'pineapples', 'strawberries']
count = 0
for element in my_list:
    print(count, my_list[count])
    count +=1
print('Done!')

#Way 2: looping through the indexes of a list w in range + for loop:
print('The list has this number of elements:',len(my_list))
for x in range(len(my_list)):
    print(x, my_list[x])

#Enumerate Function: you have access to both, index and value of each list item:

print('Enumerate() function: ')
for i, value in enumerate(my_list):
    print(i, value)

#this looks more elegant and clean!
