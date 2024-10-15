#!/usr/bin/env python3
"""
async function
"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Generate a list of 10 random numbers between 1 and 100.
    """
    return [num async for num in async_generator()]
