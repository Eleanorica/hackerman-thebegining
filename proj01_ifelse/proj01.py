# Name: Eleanor
# Date: July 9th

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
# Then, it prints out a sentence that says the number of years until they graduate.

# user_grade = raw_input("What is your grade? ")
# print "You are in year "+user_grade+"!"
# print "You will graduate high school in", 12 - int(user_grade), "years!"

# name = raw_input("Enter Name: ")
# name = name[0].upper() + name[1:].lower()
# print name

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


# If you complete extensions, describe your extensions here!

# conditional
#
# age = raw_input("What is your age?")
# if 95 > int(age) > 16:
#     print "You can drive!"
# elif int(age) == 16:
#     print "You can drive in some places!"
# elif int(age) > 95:
#     print "You are too old to drive..."
# else:
#     print "You cannot drive..."
#
# user_name = raw_input("What is your name?")
# user_month = raw_input("What is your birth month (number)?")
# user_day = raw_input("What is your birth day (number)?")
# today_month = 7
# today_day = 9
# if int(user_month) >= int(today_month):
#     print user_name+", your birthday is in", int(user_month) - int(today_month), "months"
# elif int(user_month) < int(today_month):
#     print user_name+", your birthday is in", (int(today_month) + int(user_month)) - 2, "months"
# if int(user_day) >= int(today_day):
#     print "and", int(user_day) - int(today_day), "days!"
# if int(user_day) < int(today_day):
#     print "and", 30 - (int(today_day) - int(user_day)), "days!"
#
# user_name = raw_input("What is your name?")
# user_month = raw_input("What is your birth month (number)?")
# user_day = raw_input("What is your birth day (number)?")
# today_month = 7
# today_day = 9
# if int(user_month) >= int(today_month) and int(user_day) >= int(today_day):
#     print user_name+", your birthday is in", int(user_month) - int(today_month), "months and", int(user_day) - int(today_day), "days!"
# if int(user_month) >= int(today_month) and int(user_day) < int(today_day):
#     print user_name+", your birthday is in", int(user_month) - int(today_month), "months and", 30 - (int(today_day) - int(user_day)), "days!"
# if int(user_month) < int(today_month) and int(user_day) >= int(today_day):
#     print user_name+", your birthday is in", (int(today_month) + int(user_month)) - 2, "months and", int(user_day) - int(today_day), "days!"
# if int(user_month) < int(today_month) and int(user_day) < int(today_day):
#     print user_name+", your birthday is in", (int(today_month) + int(user_month)) - 2, "months and", 30 - (int(today_day) - int(user_day)), "days!"
#
# age = raw_input("How old are you?")
# if int(age) > 16:
#     print "You can see R-rated movies!"
# if 17 > int(age) > 12:
#     print "You can see PG13-rated movies!"
# if 13 > int(age) > 7:
#     print "You can see PG-rated movies!"
# if int(age) < 8:
#     print "You can see G-rated movies!"
#
# age = raw_input("How old are you?")
# if int(age) > 16:
#     print "You can see R, PG13, PG, and G-rated movies!"
# if 17 > int(age) > 12:
#     print "You can see PG13, PG, and G-rated movies!"
# if 13 > int(age) > 7:
#     print "You can see PG and G-rated movies!"
# if int(age) < 8:
#     print "You can see G-rated movies!"
#
#
# lives = 3
# done = False
# while done == False:
#     print "Lives =", int(lives)
#     a1 = raw_input("What is 8*4? ")
#     if int(a1) == 32:
#         print "Correct!"
#     else:
#         print "Wrong!"
#         print "Lives =", (int(lives) - 1)
#         lives = (int(lives) - 1)
#
#     a2 = raw_input("Who was the first man on the moon? ")
#     if a2 == "Neil Armstrong":
#        print "Correct!"
#     else:
#         print "Wrong!"
#         print "Lives =", (int(lives) - 1)
#         lives = (int(lives) - 1)
#
#     a3 = raw_input("What year did World War II end? ")
#     if a3 == "1918":
#         print "Correct!"
#     else:
#         print "Wrong!"
#         print "Lives =", (int(lives) - 1)
#         lives = (int(lives) - 1)
#         if lives == 0:
#             print "Game Over!"
#             break
#         else:
#             continue
#
#     a4 = raw_input("How many stripes are on the American flag? ")
#     if a4 == "13":
#         print "Correct!"
#     else:
#         print "Wrong!"
#         print "Lives =", (int(lives) - 1)
#         lives = (int(lives) - 1)
#         if lives == 0:
#             print "Game Over!"
#             break
#         else:
#             continue
#
#     a5 = raw_input("How many bars are on a bar staff? ")
#     if a5 == "4":
#         print "Correct!"
#     else:
#         print "Wrong!"
#         print "Lives =", (int(lives) - 1)
#         lives = (int(lives) - 1)
#         if lives == 0:
#             print "Game Over!"
#             break
#         else:
#             continue
#
#     print "Congrats! You won!"
#     break

# 2.1 alg exercises

# list = [4, 5, 1, 3, 2]
# length = int(len(list))
# for j in range(1, length):
#     i = j - 1
#     while list[i] > list[j] and j > 0:
#         list[i], list[j] = list[j], list[i]
#         i = i - 1
#         j = j - 1
# print list


# list2 = [4, 5, 1, 3, 2]
# length = int(len(list2))
# for j in range(1, length):
#     i = j - 1
#     while list2[i] < list2[j] and j > 0:
#         list2[i], list2[j] = list2[j], list2[i]
#         i = i - 1
#         j = j - 1
# print list2


# A = [2, 7, 5, 9, 3, 1, 4, 8, 6]
# num = 1
# inlist = False
# for item in A:
#     if item == num:
#         print A.index(num)
#         inlist = True
# if inlist == False:
#     print "nil"

# p = False
# for i in range(0, length):
#     if A[i] == v:
#         print i
#         p = True
# if p == False:
#     print "nil"


def binarySearch(alist, item):
    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

print midpoint

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 8
inlist = False
length = int(len(A))
c = length/2
for item in A:
    if A[c] == num:
        print A.index(num)
        inlist = True
    elif A[c] < num:
        a
    elif A[c] > num:
        b
if inlist = False:
    print "nil"