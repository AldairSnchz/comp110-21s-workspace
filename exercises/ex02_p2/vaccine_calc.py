"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730447704"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    dtt: int = int(days_to_target(population, doses, doses_per_day, target))
    fd: str = str(future_date(days_to_target(population, doses, doses_per_day, target)))
    print("We will reach " + str(target) + "% vaccination in " + str(dtt) + " days which falls on " + fd)


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """A function that shows number of days until target."""
    perc: float = target / 100
    pernv: int = int(population * perc)
    peepv: float = doses / 2
    peepnv: float = pernv - peepv
    peepvpd: float = doses_per_day / 2
    daytilv: int = round(peepnv / peepvpd)
    return daytilv


def future_date(days_to_target: int) -> str:
    """Day vaccination goal is met."""
    hoy: datetime = datetime.today()
    daytiltar: timedelta = timedelta(days_to_target)
    date: datetime = hoy + daytiltar
    daytarmet: str = date.strftime("%B %d, %Y")
    return daytarmet


if __name__ == "__main__":
    main()
