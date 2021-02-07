"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730447704"

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

x: int = 1
y: int = 4
fortune: int = randint(x, y)
if fortune == 1:
    print("You will marry the love of your life.")
else:
    if fortune == 2:
        print("You will find inner peace.")
    else: 
        if fortune == 3:
            print("You are super cool bro.")
        else:
            print("You will have many kids.")

print("Now, go spread positive vibes!")