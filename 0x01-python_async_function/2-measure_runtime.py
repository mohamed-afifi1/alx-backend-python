#!/usr/bin/env python3
"""
runtime calculation
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n, delay) -> float:
    """
    Measure the time taken to execute n coroutines,
    """
    start_time = time.time()
    await asyncio.run(wait_n(n, delay))
    end_time = time.time()
    return (end_time - start_time) / n
