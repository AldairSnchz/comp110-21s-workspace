"""An exercise in remainders and boolean logic."""

__author__ = "730447704"


number: int = int(input("Enter an int: "))

if (number % 14) == 0:
    print("TAR HEELS")
else:
    if (number % 7) == 0:
        print("HEELS")
    else:
        if (number % 2) == 0:
            print("TAR")
        else:
            print("CAROLINA")
            

