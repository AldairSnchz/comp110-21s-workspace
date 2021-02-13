"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730447704"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")

def fortune_cookie() -> str: 
    x: int = 1
    y: int = 4
    fortune: int = randint(x, y)
    if fortune == 1:
        return "You will marry the love of your life."
    else:
        if fortune == 2:
            return "You will find inner peace."
        else:
            if fortune == 3:
                return "You are super cool bro."
            else:
                return "You will have many kids."
    

# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
