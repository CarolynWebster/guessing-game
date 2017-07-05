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
totalGuesses = 0

def checkGuess():
    guess = int(raw_input("Your guess? "))
    totalGuesses += 1
    if guess > secretNumber:
        print "Your guess is too high, try again."
        #guess = int(raw_input("Your guess? "))
    elif guess < secretNumber:
        print "Your guess is too low, try again."
        #guess = int(raw_input("Your guess? "))
    else:
        print "Well done, " + userName + "! You found my number in " + str(totalGuesses) + " tries!"

while guess != secretNumber:
    checkGuess()
