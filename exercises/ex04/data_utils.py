"""Utility functions for wrangling data."""

__author__ = "730447704"


from csv import DictReader




def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    DATA_FILE_PATH = open("data/nc_durham_2015_march_21_to_27.csv", "r", encoding="utf8")
    csv_reader = DictReader(DATA_FILE_PATH)
    for row in csv_reader:
        print(row)
    # TODO 0.1) Complete the implementation of this function here.
    DATA_FILE_PATH.close()
    return rows


# TODO: Define the other functions here.