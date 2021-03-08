"""EX03 - avoid_fifth function."""

__author__: str = "730447704"


def avoid_fifth(word: str) -> str:
    """Function that takes out e and E."""
    i = 0
    output: str = ""
    while i < len(word):
        if word[i] == "E":
            output += ""
        else: 
            if word[i] == "e":
                output += ""
            else:
                output += str(word[i])
        i += 1
    return output


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello there"))
    print(avoid_fifth("Eventually Even"))


if __name__ == "__main__":
    main()