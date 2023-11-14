"""Combining two lists intp a dictonary."""

__author__ = "730705343"


def zip(dict_str: list[str], dict_int: list[int]) -> dict[str, int]:
    """Returns a dictonary with the 2 lists combined into a dictonary."""
    dictionary: dict[str, int] = {}
    if len(dict_str) == len(dict_int):
        for i in (range(len(dict_str))):
            dictionary[dict_str[i]] = dict_int[i]
    return dictionary