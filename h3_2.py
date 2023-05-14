# START YOUR CODE HERE.
#'Write a program to prompt for a score between 0.0 and 1.0.
#If the score is out of range, print an error. If the score is
#between 0.0 and 1.0, print a grade using the following scheme:
#>= 0.9 A; >= 0.8 B; >= 0.7 C; >= 0.6 D; < 0.6 F. For the test,
#enter a score of 0.85.'

user_input = input('type a score between 0.0 and 1.0: ')
try:
    user_input = float(user_input)
    if user_input >= 0.9 :
        print('grade = A')
    elif user_input >= 0.8 :
        print('grade = B')
    elif user_input >= 0.7 :
        print('grade = C')
    elif user_input >= 0.6 :
        print('grade = D')
    elif user_input >= 0 :
        print('grade = F')
    else :
        print("No negative numbers please!")


except :
    print('Please enter a decimal!')
