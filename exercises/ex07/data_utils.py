"""Utility functions."""

__author__ = "730394749"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oritented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(col_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Shows you the first n rows of your table."""
    result: dict[str, list[str]] = {}
    for keys in col_table:
        count_list: list[str] = []
        count_list.append(keys)
    if len(count_list) + 1 <= n:
        return col_table
    else:
        for key in col_table:
            result_list: list[str] = []
            i: int = 0
            while i < n:
                result_list.append(col_table[key][i])
                i += 1
            result[key] = result_list
    return result


def select(col_table: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Selects only the rows you want based on the column names you input."""
    result: dict[str, list[str]] = {}
    i: int = 0
    while i < len(name):
        print(col_table[name[i]])
        result[name[i]] = col_table[name[i]]
        i += 1
    return result


def concat(col_table_one: dict[str, list[str]], col_table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Puts together two groups of data into one."""
    result: dict[str, list[str]] = {}
    for key_one in col_table_one:
        result[key_one] = col_table_one[key_one]
    for key_two in col_table_two:
        if key_two in result:
            i: int = 0
            while i < len(col_table_two[key_two]):
                result[key_two].append(col_table_two[key_two][i])
                i += 1
        else:
            result[key_two] = col_table_two[key_two]
    return result