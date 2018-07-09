# Name: Eleanor
# Date: July 9th

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

#user_grade = raw_input("What is your grade? ")
#print "You are in year "+user_grade+"!"
#print "You will graduate high school in", 12 - int(user_grade), "years!"

#name = raw_input("Enter Name: ")
#name = name[0].upper() + name[1:].lower()
#print name

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


# If you complete extensions, describe your extensions here!

#conditional

#age = raw_input("What is your age?")
#if 95 > int(age) > 16:
    #print "You can drive!"
#elif int(age) == 16:
    #print "You can drive in some places!"
#elif int(age) > 95:
    #print "You are too old to drive..."
#else:
    #print "You cannot drive..."

#user_name = raw_input("What is your name?")
#user_month = raw_input("What is your birth month (number)?")
#user_day = raw_input("What is your birth day (number)?")
#today_month = 7
#today_day = 9
#if int(user_month) >= int(today_month):
    #print user_name+", your birthday is in", int(user_month) - int(today_month), "months"
#elif int(user_month) < int(today_month):
    #print user_name+", your birthday is in", (int(today_month) + int(user_month)) - 2, "months"
#if int(user_day) >= int(today_day):
    #print "and", int(user_day) - int(today_day), "days!"
#if int(user_day) < int(today_day):
    #print "and", 30 - (int(today_day) - int(user_day)), "days!"

#user_name = raw_input("What is your name?")
#user_month = raw_input("What is your birth month (number)?")
#user_day = raw_input("What is your birth day (number)?")
#today_month = 7
#today_day = 9
#if int(user_month) >= int(today_month) and int(user_day) >= int(today_day):
    #print user_name+", your birthday is in", int(user_month) - int(today_month), "months and", int(user_day) - int(today_day), "days!"
#if int(user_month) >= int(today_month) and int(user_day) < int(today_day):
    #print user_name+", your birthday is in", int(user_month) - int(today_month), "months and", 30 - (int(today_day) - int(user_day)), "days!"
#if int(user_month) < int(today_month) and int(user_day) >= int(today_day):
    #print user_name+", your birthday is in", (int(today_month) + int(user_month)) - 2, "months and", int(user_day) - int(today_day), "days!"
#if int(user_month) < int(today_month) and int(user_day) < int(today_day):
    #print user_name+", your birthday is in", (int(today_month) + int(user_month)) - 2, "months and", 30 - (int(today_day) - int(user_day)), "days!"

#age = raw_input("How old are you?")
#if int(age) > 16:
    #print "You can see R-rated movies!"
#if 17 > int(age) > 12:
    #print "You can see PG13-rated movies!"
#if 13 > int(age) > 7:
    #print "You can see PG-rated movies!"
#if int(age) < 8:
    #print "You can see G-rated movies!"

#age = raw_input("How old are you?")
#if int(age) > 16:
    #print "You can see R, PG13, PG, and G-rated movies!"
#if 17 > int(age) > 12:
    #print "You can see PG13, PG, and G-rated movies!"
#if 13 > int(age) > 7:
    #print "You can see PG and G-rated movies!"
#if int(age) > 8:
    #print "You can see G-rated movies!"

lives = 3
print "Lives =", int(lives)
a_one = raw_input("What is 8*4?")
if int(a_one) == 32:
    print "Correct!"
else:
    print "Wrong!"
    print "Lives =", (int(lives) - 1)
    lives = (int(lives) - 1)

a_two = raw_input("Who was the first man on the moon?")
if a_two == "Neil Armstrong":
    print "Correct!"
else:
    print "Wrong!"
    print "Lives =", (int(lives) - 1)
    lives = (int(lives) - 1)

a_three = raw_input("What year did World War II end?")
if a_three == "1918"
    print "Correct!"
else:
    print "Wrong!"
    print "Lives =", (int(lives) - 1)
    lives = (int(lives) - 1)

if lives = 0:
    




