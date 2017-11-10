import random

number = raw_input("Enter any number between 1 and 8: ")

dice = random.randrange(1,9)
print dice
print number

if dice == number:
    print "You have won the jackpot"
else:
    print "You Lose. Better luck next time"
