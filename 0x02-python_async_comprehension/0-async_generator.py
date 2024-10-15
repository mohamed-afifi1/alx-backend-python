#!/usr/bin/env python3
"""
async function to generate random 10 numbers
"""
import asyncio
import random


async def async_generator():
    """
    Generate 10 random numbers between 1 and 100.
    """
    numbers = []
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10