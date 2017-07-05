"""A number-guessing game."""

# Put your code here
import random

print "Hey there! Let's play a game"
userName = raw_input("What's your name? ")
print userName + "I'm thinking of a number between 1 and 100. \nTry to guess my number. "

secretNumber = random.randint(1, 100)
tooHigh = 101
tooLow = 0
guess = None
totalG = 0


def checkGuess(totalG):
    guess = int(raw_input("Your guess? "))
    totalG = totalG + 1
    if guess > secretNumber:
        print "Your guess is too high, try again."
        #guess = int(raw_input("Your guess? "))
    elif guess < secretNumber:
        print "Your guess is too low, try again."
        #guess = int(raw_input("Your guess? "))
    else:
        print "Well done, " + userName + "! You found my number in " + str(totalG) + " tries!"
    return totalG
print totalG
while guess != secretNumber:
    totalG = checkGuess(totalG)
