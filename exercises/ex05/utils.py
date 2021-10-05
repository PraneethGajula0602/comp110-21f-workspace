"""List utility functions part 2."""

__author__ = "730394749"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    i: int = 0
    result: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            result.append(xs[i])
        i += 1
    return result


def sub(xs: list[int], y: int, z: int) -> list[int]:
    result: list[int] = []
    if len(xs) == 0 or y > len(xs) or z <= 0:
        return result
    if y < 0:
        y = 0
    if z > len(xs):
        z = len(xs)
    while y < z:
        result.append(xs[y])
        y += 1
    return result


def concat(xs: list[int], ys: list[int]) -> list[int]:
    i: int = 0
    j: int = 0
    result: list[int] = []
    while i < len(xs):
        result.append(xs[i])
        i += 1
    while j < len(ys):
        result.append(ys[j])
        j += 1
    return result
