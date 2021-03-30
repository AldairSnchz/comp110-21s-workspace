"""Utility functions for wrangling data."""

__author__ = "730447704"


from csv import DictReader


DATA_DIRECTORY="../../data"
DATA_FILE_PATH=f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_27.csv"


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows : list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
   
    file_handle.close()
   
    return rows       
    

def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Columns being used."""
    empty_list: list[str] = []
    for value in table:
        empty_list.append(value[key])

    return empty_list


def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Column table function."""
    empty_dict: dict[str, list[str]] = {}
    first_line: dict[str,str] = table[0]

    for value in first_line:
        empty_dict[value] = column_values(table, value)
    
    return empty_dict


def head(empty_dict: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Head of function."""
    head_dict: dict[str, list[str]] = {}

    for key in empty_dict:
        first_N_items: list[str] = []
        i: int = 0
        if rows > len(empty_dict[key]):
            rows = len(empty_dict[key])
        while i < rows:
            first_N_items.append(empty_dict[key][i])
            i += 1
        head_dict[key] = first_N_items
    
    return head_dict


def select(empty_dict: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Selects column function."""
    select_dict: dict[str, list[str]] = {}

    for key in columns:
        select_dict[key] = empty_dict[key]
    
    return select_dict


def count(frequencies: list[str]) -> dict[str, int]:
    """Counts frequencies."""
    count_dict: dict[str, int] = {}

    for key in frequencies:
        if key in count_dict:
            count_dict[key] += 1
        else:
            count_dict[key] = 1

    return count_dict

