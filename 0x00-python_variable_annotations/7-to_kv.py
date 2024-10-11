#!/usr/bin/env python3
"""
to string function
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a key-value pair to a tuple
    """
    return (k, v)
