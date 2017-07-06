"""A number-guessing game."""

# Put your code here
import random

print "Hey there! Let's play a game"
userName = raw_input("What's your name? ")


def checkGuess(secretNumber, totalG):
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
            #print "Your best guess count was %".format(best_score)
    else:
        print "That guess is outside of the range!"
    return guess


def in_range(guess):
    """decides if guess is within range of 1:101"""
    if guess > 0 and guess < 101:
        return True
    return False


def start_new_game():
    print userName + " I'm thinking of a number between 1 and 100. \nTry to guess my number. "
    secretNumber = random.randint(1, 100)
    guess = None
    totalG = 0

    while guess != secretNumber:
        totalG += 1
        guess = checkGuess(secretNumber, totalG)
    return totalG

#def find_best_score():
 #   if best_score is not None:



best_score = None
total_games = 1
keep_playing = True
start_new_game()
while keep_playing is True:
    play_again = raw_input("Would you like to play again? Y or N? ")
    if play_again == "Y" or play_again == "y" or play_again == "N" or play_again == "n":
        if play_again == "Y" or play_again == "y":
            total_games += 1
            start_new_game()
        else:
            print "Thanks for playing! You have played " + str(total_games) + " games!"
            print "The best score was @@@@"
            break
    else:
        print "That is not a valid response."
