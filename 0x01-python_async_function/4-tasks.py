#!/usr/bin/env python3
"""
async routine n times
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait a random number of seconds
    """
    tasks = []
    delays = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
