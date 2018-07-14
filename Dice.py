import random
play = False
while play == False:
    p1_win = False
    p2_win = False
    print "If the dice roll is odd, player one wins. If it's odd, player two wins."
    rand_int = random.randint(1, 6)
    if rand_int == 1:
        print " _______"
        print "|       |"
        print "|   o   |"
        print "|       |"
        print " ------- "
    elif rand_int == 2:
        print " _______"
        print "| o     |"
        print "|       |"
        print "|     o |"
        print " ------- "
    elif rand_int == 3:
        print " _______"
        print "| o     |"
        print "|   o   |"
        print "|     o |"
        print " ------- "
    elif rand_int == 4:
        print " _______"
        print "| o   o |"
        print "|       |"
        print "| o   o |"
        print " ------- "
    elif rand_int == 5:
        print " _______"
        print "| o   o |"
        print "|   o   |"
        print "| o   o |"
        print " ------- "
    elif rand_int == 6:
        print " _______"
        print "| o   o |"
        print "| o   o |"
        print "| o   o |"
        print " ------- "
    if rand_int == 1 or rand_int == 3 or rand_int == 5:
        p1_win = True
    else:
        p2_win = True
    if p1_win == True:
        print "Player 1 wins!"
    elif p2_win == True:
        print "Player 2 wins!"
    play_again = raw_input("Do you want to roll again? (y/n)" )
    if play_again == "n":
        exit()
    else:
        play = False