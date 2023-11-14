"""Test my zip function."""

__author__ = "730704343"

from lessons.zip import zip

def test_lists_not_equal():
    """Testing to see if the two lists are equal."""
    dict_str: list[str] = ["apples", "oranges", "grapes"]
    dict_int: list[int] = [1, 2]
    assert zip(dict_str, dict_int) == {}

def test_empty_list():
    """Testing to see that an empty dict is returned if input lists are empty."""
    dict_str = list()
    dict_int = list()
    assert zip(dict_str, dict_int) == {}

def test_equal_list():
    """Testing to see that the dictionary works when equal lists are inputted."""
    dict_str: list[str] = ["apples", "oranges"]
    dict_int: list[int] = [1 ,2]
    assert zip(dict_str, dict_int) == {"apples": 1, "oranges": 2}