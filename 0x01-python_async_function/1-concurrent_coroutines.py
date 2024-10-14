#!/usr/bin/env python3
"""
async routine n times
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay) -> List[float]:
    """
    wait a random number of seconds
    """
    tasks = []
    delays = []
    for _ in range(n):
        task = wait_random(max_delay)
        tasks.append(task)
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
