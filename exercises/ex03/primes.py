"""EX03 - prime functions."""

__author__: str = "730447704"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(3))
    print(is_prime(6))
    print(is_prime(31))
    print(is_prime(110))
    print(list_primes(3, 7))
    print(list_primes(10, 20))
    print(list_primes(25, 28))
    print(list_primes(-1, 5))


def is_prime(num: int) -> bool:
    """Figures out if the number is prime or not"""
    i = 2
    while i < num:
        div: int = num % i
        if div == 0:
            return False
        i += 1
    if num < 2:
        return False
    else:
        return True


def list_primes(first: int, last: int) -> list[int]:
    """Lists the primes"""
    i = first
    list_nums: list[int] = []
    while i < last:
        list_nums.append(i)
        i += 1
    i = 0
    plist: list[int] = []
    while i < len(list_nums):
        if list_nums[i] > 1:
            if is_prime(list_nums[i]) is True:
                plist.append(list_nums[i])
        i += 1
    return plist


if __name__ == "__main__":
    main()