# Guessing Game v1.0 by Matthew Comensoli (u7202599)
# For COMP7230 - Assignment 1, Group BJ
# Idea for guessing game inspired by:
# https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/
# Information on the random library found at:
# https://docs.python.org/3/library/random.html

import random

CorrectAnswer = random.randint(1, 1000)
Guess = 1

print("I'm thinking of a number between 1 and 1000.\nYou have 10 guesses. Good luck!\n")

# While loop breaks on correct answer or after 10th guess

while Guess < 11:

# Added try statement to prevent input that wasn't a valid integer

    try:
        x = int(input("Guess number {}: ".format(Guess)))

    except:
        print("Sorry - please enter a valid number.\n")
        continue

# Made a separate if statement for guess 10, so print command wasn't "1 guesses remaining"

    if x > CorrectAnswer:
        Guess = Guess + 1
        if Guess == 10:
            print("Too High! Only one chance left\n")
        else:
            print("Too High! You have {} guesses remaining\n".format(11 - Guess))

    if x < CorrectAnswer:
        Guess = Guess + 1
        if Guess == 10:
            print("Too Low! Only one chance left\n")
        else:
            print("Too Low! You have {} guesses remaining\n".format(11 - Guess))

    if x == CorrectAnswer:
        break

# Three possible results - found number on first attempt, found number, or didn't find number within 10 guesses

if Guess == 1:
    print("Congratulations - you got it first go! The number was {}.".format(CorrectAnswer, Guess))

elif x == CorrectAnswer:
    print("Congratulations! The number was {}.\nYou took {} guesses to find the answer.".format(CorrectAnswer, Guess))

elif x != CorrectAnswer:
    print("Sorry, you lose!")

