#!/usr/bin/env python3
"""
return random wait
"""
import random
import asyncio


async def wait_random(max_delay=10) -> float:
    """
    Wait a random amount of time up to max_delay seconds.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
