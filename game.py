"""A number-guessing game."""

# Put your code here
import random

print "Hey there! Let's play a game"
userName = raw_input("What's your name? ")
print userName + " I'm thinking of a number between 1 and 100. \nTry to guess my number. "

secretNumber = random.randint(1, 100)
guess = None
totalG = 0


def checkGuess():
    """Decides if guess is numerical or correct"""
    try:
        guess = int(raw_input("Your guess? "))
    except:
        print "You fool! That's not a number!"
        return
    if in_range(guess):
        if guess > secretNumber:
            print "Your guess is too high, try again."
        elif guess < secretNumber:
            print "Your guess is too low, try again."
        else:
            print "Well done, " + userName + "! You found my number in " + str(totalG) + " tries!"
    else:
        print "That guess is outside of the range!"
    return guess


def in_range(guess):
    """decides if guess is within range of 1:101"""
    if guess > 0 and guess < 101:
        return True
    return False


while guess != secretNumber:
    totalG += 1
    guess = checkGuess()
