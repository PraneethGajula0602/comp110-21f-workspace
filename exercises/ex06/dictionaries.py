"""Practice with dictionaries."""

__author__ = "730394749"

# Define your functions below


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the key and values of a given dictionary."""
    result = dict()
    for key in x:
        if x[key] in result:
            raise KeyError("KeyError")
        result[x[key]] = key
    return result


def favorite_color(x: dict[str, str]) -> str:
    """Finds the most liked color in a given dictionary."""
    y: dict[str, int] = dict()
    for key in x:
        if x[key] in y:
            y[x[key]] += 1
        else:
            y[x[key]] = 1
    greatest: int = 0
    for new in y:
        if y[new] >= greatest:
            greatest = y[new]
    result: str = ""
    for color in y:
        if greatest == y[color]:
            result = color
        if result != "":
            return result


print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Praneeth": "blue"}))


def count(x: list[str]) -> dict[str, int]:
    """Shows how frequently each item in a list shows up."""
    result: dict[str, int] = {}
    i: int = 0
    a: int = len(x)
    while i < a:
        if x[i] in result:
            result[x[i]] += 1
        else:
            result[x[i]] = 1
        i += 1
    return result