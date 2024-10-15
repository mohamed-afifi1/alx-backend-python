#!/usr/bin/env python3
"""
measure_runtime
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the runtime of four functions
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(), async_comprehension(),
        async_comprehension(), async_comprehension())
    return time.time() - start_time
