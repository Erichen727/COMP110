"""EX04 - List Utility Functions."""
__author__ = "730705343"


def all(list_num: list[int], num: int) -> bool:
    """Returns a boolean for if all the numbers in the list match the integer."""
    counter: int = 0
    if len(list_num) == 0:
        return False
    # loop to check if each numnber in the list is the given integer.
    while counter < len(list_num):
        if num != list_num[counter]:
            return False
        counter += 1
    return True


def max(list_nums: list[int] = list()) -> int:
    """Returns the highest number in the given list."""
    if len(list_nums) == 0:
        raise ValueError("max() arg is an empty List")
    counter: int = 0
    max_num = list_nums[0]
    # loop to check for highest number.
    while counter < len(list_nums):
        if list_nums[counter] > max_num:
            max_num = list_nums[counter]
        counter += 1
    return max_num


def is_equal(list1: list[int] = list(), list2: list[int] = list()) -> bool:
    """Returns a boolean for if all the numbers in two lists match."""
    counter: int = 0
    if len(list1) != len(list2):
        return False
    # checks to see if number and order matches.
    while counter < len(list1) and counter < len(list2):
        if list1[counter] != list2[counter]:
            return False
        if list1[counter] == list2[counter]:
            counter += 1
    return True