"""List utility functions."""

__author__ = "730394749"


# TODO: Implement your functions here.


def all(a: list[int], b: int) -> bool:
    """Figure out if all of a is the same as b."""
    length: int = len(a)
    if length == 0:
        return False
    i: int = 0
    while i < length:
        if a[i] != b:
            return False
        else:
            i = i + 1
    return True


def is_equal(a: list[int], b: list[int]) -> bool:
    """Figure out if two lists are equal."""
    length_one: int = len(a)
    length_two: int = len(b)
    if length_one != length_two:
        return False
    if length_one < length_two:
        return False
    else:
        i: int = 0
        while i < length_one:
            if a[i] != b[i]:
                return False
            else:
                i = i + 1
        return True


def max(a: list[int]) -> int:
    """Find the largest value in a given set of values."""
    if len(a) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        greatest: int = a[0]
        i: int = 0
        while i < len(a):
            if a[i] >= greatest:
                greatest = a[i]
            i = i + 1
        return greatest