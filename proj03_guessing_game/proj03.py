# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random

print "I'm thinking of a number between 1 and 30. Can you guess my number?"
my_num = random.randint(0,30)
guesses = 0
done = False
while done == False and guesses <= 6:
    num = raw_input("Guess a number or enter END to quit the game.")
    if num == "END":
        print "Thanks for playing. You had guessed", guesses, "times before you quit."
        done = True
    elif int(num) < my_num:
        print "Your number is too low!"
        guesses += 1
    elif int(num) > my_num:
        print "Your number is too high!"
        guesses += 1
    else:
        guesses += 1
        print "Congrats on guessing the number! You used", guesses, "guesses to win the game."
        done = True
        ans = int(raw_input("If you want to play again, type 1 and enter."))
        if ans == 1:
            guesses = 0
            done = False
if guesses > 6:
    print "Thanks for playing, but you reached the maximum number of guesses before you won. The correct answer was", my_num