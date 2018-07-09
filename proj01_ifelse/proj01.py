# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

#user_grade = raw_input("What is your grade? ")
#print "You are in year "+user_grade+"!"
#print "You will graduate high school in", 12 - int(user_grade), "years!"

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


# If you complete extensions, describe your extensions here!

#conditional

#age = raw_input("What is your age?")
#if int(age) > 16:
    #print "You can drive!"
#elif int(age) == 16:
    #print "You can drive in some places!"
#elif int(age) > 95:
    #print "You are too old to drive..."
#else:
    #print "You cannot drive..."

user_name = raw_input("What is your name?")
#user_month = raw_input("What is your birth month (number)?")
user_day = raw_input("What is your birth day (number)?")
#today_month = 7
oday_day = 9
#if int(user_month) >= int(today_month):
    #print user_name+", your birthday is in", int(user_month) - int(today_month), "months"
#elif int(user_month) < int(today_month):
    #print user_name+", your birthday is in", (int(today_month) + int(user_month)) - 2, "months"

if int(user_day) >= int(today_day):
    print "and", int(user_day) - int(today_day), "days!"
elif int(user_day) < int(today_day):
    print "and", 30 - (int(today_day) - int(today_day)), "days!"


#user_name = raw_input("What is your name?")
#user_month = raw_input("What is your birth month (number)?")
#user_day = raw_input("What is your birth day (number)?")
#today_month = 7
#today_day = 9
#if int(user_month) >= int(today_month) and int(user_day) >= int(today_day):
    #print user_name+", your birthday is in", int(user_month) - int(today_month), "months and", int(user_day) - int(today_day), "days!"
#if int(user_month) >= int(today_month) and int(user_day) < int(today_day):
    #print user_name+", your birthday is in", int(user_month) - int(today_month), "months and", 30 - (int(today_day) - int(today_day)), "days!"
#if int(user_month) < int(today_month) and int(user_day) >= int(today_day):
    #print user_name+", your birthday is in", (int(today_month) + int(user_month)) - 2, "months and", int(user_day) - int(today_day), "days!"
#if int(user_month) < int(today_month) and int(user_day) < int(today_day):
    #print user_name+", your birthday is in", (int(today_month) + int(user_month)) - 2, "months and", 30 - (int(today_day) - int(today_day)), "days!"