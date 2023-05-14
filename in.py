#in as a logical operator:
#String Library: Python has a number of String
#functions already built into every String
while True :
    word = input("Type the word (to end type: done): ")
    if word == "done" :
        break
    letter = input("Type the letter: ")

    if letter.lower() in word.lower() :
        print("The letter is in the word!")
    else :
        print("The letter is not in the word!")
print("Programm end")
