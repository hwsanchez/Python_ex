#continue is another loop-control statement (like break) that will go back to the top of the loop
#continue says: 'stop this iteration'; in this case there will be no print-out when we type #*
#Loops with while are called indefinite Loops
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('finished!')
