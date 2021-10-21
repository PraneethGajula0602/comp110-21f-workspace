"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730394749"


def test_invert_one() -> None:
    """Testing invert with a use case."""
    x: dict = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(x) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_two() -> None:
    """Testing invert with a use case."""
    x: dict = {'cat': 'meow', 'dog': 'woof', 'duck': 'quack'}
    assert invert(x) == {'meow': 'cat', 'woof': 'dog', 'quack': 'duck'}


def test_invert_three() -> None:
    """Testing invert with a edge case."""
    x: dict = {'Algebra': 'Math', 'Calculus': 'Math', 'Python': 'Comp'}
    assert invert(x) == 'KeyError'


def test_favorite_color_one() -> None:
    """Testing favorite_color with a use case."""
    x: dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Praneeth": "yellow"}
    assert favorite_color(x) == "yellow"


def test_favorite_color_two() -> None:
    """Testing favorite_color with a use case."""
    x: dict = {"Ben": "white", "Jerry": "blue", "Chris": "white", "Chase": "red"}
    assert favorite_color(x) == "white"


def test_favorite_color_three() -> None:
    """Testing favorite_color with an edge case."""
    x: dict = {"Kevin": "red", "Bob": "green", "Max": "blue", "Terry": "orange"}
    assert favorite_color(x) == "red"


def test_count_one() -> None:
    """Testing count with a use case."""
    x: list = ["a", "b", "c", "b", "b", "a"]
    assert count(x) == {'a': 2, 'b': 3, 'c': 1}


def test_count_two() -> None:
    """Testing count with a use case."""
    x: list = ["a", "b", "c"]
    assert count(x) == {'a': 1, 'b': 1, 'c': 1}


def test_count_three() -> None:
    """Testing count with an edge case."""
    x: list = ["a", "b", "c", "d", "e", "e"]
    assert count(x) == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2}
