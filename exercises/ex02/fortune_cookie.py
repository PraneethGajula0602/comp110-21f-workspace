"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730394749"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
r1 = randint(1, 4)
if r1 == 1:
    print("You will see the person you most desire today.")
else:
    if r1 == 2:
        print("You will get a great opportunity today.")
    else:
        if r1 == 3:
            print("You will receive a lot of money today.")
        else:
            if r1 == 4:
                print("Something unexpected will happen to you today.")
print("Now, go spread positive vibes!")