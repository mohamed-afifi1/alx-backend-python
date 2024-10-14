#!/usr/bin/env python3
"""
send task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(delay: int) -> asyncio.Task:
    """
    Wait a random amount of time up to max_delay seconds.
    """
    return asyncio.create_task(wait_random(delay))
