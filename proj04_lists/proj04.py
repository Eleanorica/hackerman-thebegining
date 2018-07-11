# coding=utf-8
# Name:
# Date:

# var = []
# var2 = [1, 2, 3, 4]
# var3 = ["a", "b", "cat", 3]

# index- 0 indexed
# one item
# print var3[2]

# slice of list
# print var2[0:2]
# all but first item
# print var3[1:]
# all but last item
# print var3[:-1]

# replace
# var2[0] = "man"
# print var2

# loop
# to change
# counter = 0
# for item in var3:
    # if item == "cat":
        # var3[counter] = "dog"
    # elif item == 3:
        # var3[counter] = "flower"
    # counter = counter + 1
    # print var3

# add to list
# var3.append("girl")
# print var3

# lst = []
# s = "This is a string"
# for letter in s:
    # lst.append(letter)
# print lst

"""
proj04

practice with lists

"""

# Part I
# Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
# ext 1
# aa = []
# counter = 0
# for item in a:
#     if item < 5:
#         print a[counter]
#         aa.append(a[counter])
#         counter = counter + 1
# print aa

# ext 2
# high = int(raw_input("Enter a number"))
# aa = []
# counter = 0
# for item in a:
#     if item < high:
#         aa.append(a[counter])
#         counter = counter + 1
# print aa


# Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

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

# ext 1

# import random
# aaa = []
# bbb = []
# ccc = []
#
# counter = 0
# listlength = random.randint(1, 50)
# while counter < listlength:
#     numa = random.randint(1, 100)
#     aaa.append(numa)
#     counter = counter + 1
# print "List 1:",aaa
#
# counter = 0
# listlength = random.randint(1, 50)
# while counter < listlength:
#     numb = random.randint(1, 100)
#     bbb.append(numb)
#     counter = counter + 1
# print "List 2:",bbb
#
# counter = 0
# valueaaa = list(set(aaa))
# valuebbb = list(set(bbb))
# for item in valueaaa:
#     if item in valuebbb:
#         ccc.append(valueaaa[counter])
#     counter = counter + 1
# print "Common numbers:",ccc


# if 8 in b:
#     print 8

# len(aaa)

# Part III
# Take a list, say for example this one:

# d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# # and write a program that replaces all “a” with “*”.
#
# counter = 0
# for item in d:
#     if item == "a":
#         d[counter] = "*"
#     counter = counter + 1
# print d


# Part IV
# Ask the user for a string, and print out whether this string is a palindrome or not.

# counterr = 0
# counter = 0
# word = raw_input("Type in a word and I will tell you if it is a palindrome!")
# word = word[0:].lower()
# wordlist = []
# length = int(len(wordlist))
# for item in wordlist:
#     if item == " ":
#         wordlist[counterr] = ""
#     counterr = counterr + 1
# for letter in word:
#     wordlist.append(letter)
# if wordlist[0] != wordlist[-1]:
#     print "It is not a palindrome!"
#     exit()
# while counter < (length/2):
#     if wordlist[0] == wordlist[-1]:
#         wordlist = wordlist[1:-1]
#         counter = counter + 1
# print "It is a palindrome!"