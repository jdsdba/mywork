#!/usr/bin/python3
round = 0
answer = " "

while round < 3 and not (answer.lower() == "brian" or answer.lower() == 'shrubbery'):
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if answer.lower() == "brian": # logic to check if user gave correct answer
        print("Correct!")
    elif answer.lower() == "shrubbery": # logic to check if user gave correct answer
        print("You gave the super secret answer!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")

