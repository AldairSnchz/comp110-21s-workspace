"""EX03 - palindromify function."""

__author__: str = "730447704"


def palindromify(statement: str, one_two: bool) -> str:
    """Creates the palindromify"""
    word: str = statement
    if one_two is True:
        i = len(statement)
        while i > 0:
            i = i - 1
            word += statement[i]
    else:
        i = len(statement) - 1
        while i > 0:
            i = i - 1
            word += statement[i]
    return word


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time", False))


if __name__ == "__main__":
    main()