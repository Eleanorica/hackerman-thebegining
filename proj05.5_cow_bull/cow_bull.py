# Create a program that will play the 'cows and bulls' game with the user. The game works
# like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every
# digit that the user guessed correctly in the correct place, they have a 'cow'. For
# every digit the user guessed correctly in the wrong place is a 'bull.' Every time the
# user makes a guess, tell them how many 'cows' and 'bulls' they have. Once the user
# guesses the correct number, the game is over. Keep track of the number of guesses the
# user makes throughout the game and tell the user at the end.
#
# Say the number generated by the computer is 1038. An example interaction could look like
# this:
#
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull

# Until the user guesses the number.


import random
number = str(random.randint(1000,9999)) #random 4 digit number

numberlist = []
for letter in number:
    numberlist.append(letter)

print "Welcome ot the cows and bulls game!"
user_guess = raw_input("Guess a four digit number or type exit to leave.")
if user_guess == "exit":
    exit()

usernumberlist = []
for letter in user_guess:
    usernumberlist.append(letter)


b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# high = int(raw_input("enter a number"))
# aa = []
# counter = 0
# for item in a:
#     if item < high:
#         print a[counter]
#         aa.append(a[counter])
#         counter = counter + 1
# print aa

# bc = []
# counter = 0
# valueb = list(set(b))
# valuec = list(set(c))
# for item in valueb:
#     if item in valuec:
#         bc.append(valueb[counter])
#     counter = counter + 1
# print bc


# import random
# aaa = []
# bbb = []
# ccc = []
#

#
# counter = 0
# valueaaa = list(set(aaa))
# valuebbb = list(set(bbb))
# for item in valueaaa:
#     if item in valuebbb:
#         ccc.append(valueaaa[counter])
#     counter = counter + 1
# print "Common numbers:",ccc
