"""My Guessing game!"""


from random import randint


__author__ = "730447704"


intr: str = "In this game you will be trying to guess the letter i'm thinking of"
other: str = "please choose which option you would like"
the_three: str = "1: Main game, 2: Bonus game, or 3: Main menu"
mad_emoji: str = "\U0001F643"
my_emoji: str = "\U0001F605"                # 7 emoji global variables
end_emoji: str = "\U0001F44D"
player: str                                 # Player global variable
op_one: str = "You will now try to guess what letter im thinking of in the fewest attempts"
points: int


def main() -> None:                         # 0 Main function that returns none
    """Where everything is going down."""
    print(greet())
    option: int = int(input("Option? "))
    points: int = 0
    if option == 1:                         # 3 presenting three options and taking you to them
        print(option_one())
        print(extra_option())
    else:
        if option == 2:
            print(option_two(points))
            print(f"Your final score is -1 because you didn't even try {mad_emoji}")
        else:
            print(option_three())


def greet() -> None:                            # 1 Procedure nameed greet
    """Greeting to the player and introduction."""
    player: str = str(input("What is your name? "))
    print(f"Hello {player} and welcome to my guessing game! {intr}, {other}, {the_three}.")
    return None


def option_one() -> str:              # 4 procedure call
    """This is where the game will take place."""
    print(f"Great this is the main game! {op_one}")
    points: int = 0
    while input("Letter? ") != "g":
        print(f"Not Quite {my_emoji} Keep guessing!")
        points += 1
        print(f"{points} try/tries")
    return f"Congratulations, you got it in {points + 1} attempt(s) {end_emoji}" 


def extra_option() -> str:
    """This will ask if the player wants to play a bonus round."""
    points: int = 0
    print("Would you like to play a bonus round?")
    response: str = str(input("yes or no? "))
    if response == "yes":
        return(f"Your final score is {option_two(points)}! ")
    else:
        return "Okay that's fine, have a good day!"


def option_two(a: int) -> int:                  # 5 function with int parameter and return int
    """This is the bonus round."""
    points: int = int(input("How many tries did the first round take? "))
    if a < 10:
        return points - 1
    else:
        return points + 1


def option_three() -> str:
    """Prints adventure points and says goodbye."""
    points: int = 0                 # 2 points in main
    x: int = 1
    y: int = 3
    leave: int = randint(x, y)              # 8 random
    if leave == 1:
        return f"You took {points} guesses so you must be good! Come again soon!"       # 6 f string
    else:
        if leave == 2:
            return f"{points} guesses, you should have tried my game {mad_emoji}"
        else:
            return f"You suck, you took {points} guesses and didn't even try {mad_emoji}"


if __name__ == "__main__":      
    main()