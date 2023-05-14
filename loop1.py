#Breaking out of a while loop in Phyton
#While is an indefinite Loop, because they keep going untul a logical condition is true
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('done!')
