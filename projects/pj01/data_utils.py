from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a table."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the csv line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def head(col_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Shows you the first n rows of your table."""
    result: dict[str, list[str]] = {}
    for key in col_table:
        count_list: list[str] = []
        i: int = 0
        if len(col_table[key][0]) < n:
            n = len(col_table[key][0])
        while i < n:
            count_list.append(col_table[key][i])
            i += 1
        result[key] = count_list
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


def select(col_table: dict[str, list[str]], name: list[str]) -> dict[str, list[str]]:
    """Selects only the rows you want based on the column names you input."""
    result: dict[str, list[str]] = {}
    i: int = 0
    while i < len(name):
        print(col_table[name[i]])
        result[name[i]] = col_table[name[i]]
        i += 1
    return result


def count(data: list[str]) -> dict[str, int]:
    """Tells you how many times an item is in a list."""
    result: dict[str, int] = {}
    for key in data:
        if key in result:
            result[key] = result[key] + 1
        else:
            result[key] = 1
    return result


def total(data: dict[str, list[str]], value_column: str, name_column: str, name_one: str, name_two: str, name_three: str) -> dict[str, int]:
    """This function takes the totals of the values for two names under a column."""
    result: dict[str, int] = {name_one: 0, name_two: 0, name_three: 0}
    i: int = 0
    while i < len(data[value_column]):
        rating: int = int((data[value_column])[i])
        if data[name_column][i] == name_one:
            result[name_one] += rating
        elif data[name_column][i] == name_two:
            result[name_two] += rating
        else:
            result[name_three] += rating
        i += 1
    return result


def average(names: dict[str, int], totals: dict[str, int]) -> dict[str, float]:
    """Given two dictionaries, this function will spit out the average of one value divided by the other."""
    result: dict[str, float] = {}
    if len(names) != len(totals):
        print("Dictionaries are of differing lengths.")
    for key in names:
        result[key] = totals[key] / names[key]
    return result