"""Summing the elements of a list using different loops."""

__author__ = "730705343"


def w_sum(list_nums: list[float]) -> float:
    """Adds all the numbers in the list using a while loop."""
    counter = 0
    total_sum: float = 0.0
    while counter < len(list_nums):
        total_sum += list_nums[counter]
        counter += 1
    return (total_sum)


def f_sum(list_nums: list[float]) -> float:
    """Adds all the numbers in a list using a for ... in loop."""
    total_sum: float = 0.0
    for item in list_nums:
        total_sum += item
    return (total_sum)


def f_range_sum(list_nums: list[float]) -> float:
    """Adds all the numbers in a list using a for ... in range... loop."""
    total_sum: float = 0.0
    for item in range(0, len(list_nums)):
        total_sum += list_nums[item]
    return total_sum
        
