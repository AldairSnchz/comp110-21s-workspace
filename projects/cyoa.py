"""My Guessing game"""

def greet() -> None:                            #1 Procedure nameed greet
    """Greeting to the player and introduction."""
    print("Hello and welcome to my guessing game!")
    print("In this game you will be trying to guess the letter or number im thinking of")
    player: str = str(input("Name? "))
    print(f"{player} please choose which option you would like")
    print("1: Letter, 2: Number, Or 3: Main menu")



def experience(choice: int) -> str: 
    if choice == 1:
        return "Great lets get started"
    else:
        if choice == 2:
            return "Say less homie"
        else:
            return "You took 0 guesses, Have a nice day"



def main() -> None:                         #0 Main function that returns none
    print(greet())
    option: int = int(input("Option? "))
    print(experience(option))
    points: int = 0
    easy_letter: str = str(input("Letter? "))



if __name__ == "__main__":      
    main()
