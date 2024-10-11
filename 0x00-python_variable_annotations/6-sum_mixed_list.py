#!/usr/bin/env python3
"""
to string function
"""
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """
    Calculate the sum of all elements in a list
    """
    total = 0
    for num in input_list:
        total += num
    return total
