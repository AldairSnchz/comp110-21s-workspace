"""A vaccination calculator."""

__author__ = "730447704"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

people: int = int(input("Population: "))
doses_admin: int = int(input("Doses administered: "))
dad: int = int(input("Doses per day: "))
target_per_vaccinated: int = int(input("Target percent vaccinated: "))

percentage: float = target_per_vaccinated / 100
percent_not_vac: int = int(people * percentage)
people_vac: float = doses_admin / 2
people_need_vac: float = percent_not_vac - people_vac
people_vac_per_day: float = dad / 2
days_until_vac: int = round(people_need_vac / people_vac_per_day)

today_date: datetime = datetime.today()
days_until_target_per_vaccinated: timedelta = timedelta(days_until_vac)
date: datetime = today_date + days_until_target_per_vaccinated
day_complete_target: str = date.strftime("%B %d, %Y")
print("We will reach " + str(target_per_vaccinated) + "% vaccination in " + str(days_until_vac) + " days, which falls on " + day_complete_target)
