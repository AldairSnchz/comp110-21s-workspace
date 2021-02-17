"""Tar Heels exercise redux as a structured program."""

__author__ = "730447704"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(response: int) -> str:
    """Dividing numbers."""
    if (response % 14) == 0:
        return "TAR HEELS"
    else:
        if (response % 7) == 0:
            return "HEELS"
        else:
            if (response % 2) == 0:
                return "TAR"
            else:
                return "CAROLINA"


if __name__ == "__main__":
    main()
