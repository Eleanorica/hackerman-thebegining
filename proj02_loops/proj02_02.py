# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

#key word is "for"
#loop over a range of numbers

# sum = 0
# for num in range (0,9):
#     sum = sum + num
#     print sum


#loop over strings

# s = "vsa"
# for letter in s:
#     print letter
#     if letter == "s":
#         print "This is an s"


# prev = 0
# curr = 1
# nxt = 1
# thismany = raw_input("How many Fibonacci numbers should I generate?")
# for num in range (0,int(thismany)):
#     print curr
#     nxt = curr + prev
#     prev = curr
#     curr = nxt


# s = 0
# p = 0
# c = 1
# n = 1
# thismany = raw_input("How many Fibonacci numbers should I generate?")
# while s < int(thismany):
#     print c
#     n = c + p
#     p = c
#     c = n
#     s = s + 1


# prev = 0
# curr = 1
# thismany = raw_input("How many Fibonacci numbers should I generate?")
# for num in range (0,int(thismany)):
#     print curr
#     curr = curr + prev
#     prev = curr - prev


# prev = 0
# curr = 1
# nxt = 1
# thismany = raw_input("How many powers of 2 should I generate?")
# for num in range (0,int(thismany)):
#     print curr
#     nxt = curr*2
#     prev = curr
#     curr = nxt


# counter = 1
# thisone = int(raw_input("Input a number and I will find all of the divisors!"))
# while counter <= thisone:
#     if thisone % counter == 0:
#         print counter
#     counter = counter + 1