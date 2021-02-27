"""My hangman game"""

def greet() -> None:
    """Greeting to the player and introduction."""
    print("Hello and welcome to my Hangman game!")
    print("In this game you will be trying to guess the word one letter at a time")
    player: str = str(input("Name? "))
    print(f"{player} please choose which option you would like")
    print("1: Easy, 2: Hard, Or 3: Main menu")


def experience(choice: int) -> str: 
    if choice == 1:
        return "Great lets get started"
    else:
        return "Maybe next time"



def main() -> None: 
    print(greet())
    option: int = int(input("Option? "))
    print(experience(option))


if __name__ == "__main__": 
    main()
