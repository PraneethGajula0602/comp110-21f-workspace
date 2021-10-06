"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730394749"


def test_only_evens_one() -> None:
    """Testing only_evens for an empty set."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_two() -> None:
    """Testing only_evens for a use case."""
    xs: list[int] = [1, 2, 4, 5]
    assert only_evens(xs) == [2, 4]


def test_only_evens_three() -> None:
    """Testing only_evens for a set with only odd numbers."""
    xs: list[int] = [1, 3, 5, 7]
    assert only_evens(xs) == []


def test_sub_one() -> None:
    """Testing sub for an empty set."""
    xs: list[int] = []
    y: int = 1
    z: int = 3
    assert sub(xs, y, z) == []


def test_sub_two() -> None:
    """Testing sub for a use case."""
    xs: list[int] = [1, 2, 3, 4, 5]
    y: int = 2
    z: int = 4
    assert sub(xs, y, z) == [3, 4]


def test_sub_three() -> None:
    """Testing sub for the given example."""
    xs: list[int] = [10, 20, 30, 40]
    y: int = 1
    z: int = 3
    assert sub(xs, y, z) == [20, 30]


def test_concat_one() -> None:
    """Testing concat for an empty set."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_two() -> None:
    """Testing concat for a use case."""
    xs: list[int] = [1, 2, 3, 4]
    ys: list[int] = [5, 6, 7, 8]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_three() -> None:
    """Testing concat for a use case."""
    xs: list[int] = [1, 3, 5, 7]
    ys: list[int] = [2, 4, 6, 8]
    assert concat(xs, ys) == [1, 3, 5, 7, 2, 4, 6, 8]