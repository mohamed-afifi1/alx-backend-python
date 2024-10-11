#!/usr/bin/env python3
"""
to string function
"""


def sum_list(list: list[float]) -> float:
    """
    Calculate the sum of all elements in a list
    """
    total = 0
    for num in list:
        total += num
    return total
