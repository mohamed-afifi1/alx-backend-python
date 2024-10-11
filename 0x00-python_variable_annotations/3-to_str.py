#!/usr/bin/env python3
"""
to string function
"""


def to_string(n: float) -> str:
    """
    Convert a float number to a string representation,
    without using built-in functions or libraries for string manipulation.
    """
    # Check if the number is negative
    negative = False
    if n < 0:
        negative = True
        n = -n

    # Convert the integer part to a string
    integer_part = int(n)
    integer_str = ""

    # Convert the fractional part to a string
    fractional_part = n - integer_part
    fractional_str = ""

    # Convert the integer part to a string
    while integer_part > 0:
        digit = integer_part % 10
        integer_str = str(digit) + integer_str
        integer_part //= 10

    # Convert the fractional part to a string
    while fractional_part > 0:
        fractional_part *= 10
        digit = int(fractional_part)
        fractional_str += str(digit)
        fractional_part -= digit
    if(negative):
        return "-" + integer_str + "." + fractional_str
    else:
        return integer_str + "." + fractional_str
