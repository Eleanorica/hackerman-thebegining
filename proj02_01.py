# Name: Eleanor
# Date: July 10

# proj02: sum

# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.

#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers is: 21

# key word is while


# counter = 0
#
# while counter <= 10:
#     print counter
#     counter = counter + 1


#counter = 0
# s = ""

#while counter <= 10:
    #print counter
    #counter = counter + 1
    #s = s + "a"
    #print s
    #if counter == 5:
        #break

a1 = raw_input("Enter a number to sum, or 0 to indicate you are done.")
counter = int(a1)
while int(a1) != 0:
    a1 = raw_input("Enter a number to sum, or 0 to indicate you are done.")
    counter = counter + int(a1)
print counter


