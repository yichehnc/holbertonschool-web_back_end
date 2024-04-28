#!/usr/bin/env python3
"""
A coroutine called async_comprehension that takes no arguments
"""
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """
    A coroutine called async_comprehension that takes no arguments
    and returns the 10 random numbers
    """
    async_generator = __import__('0-async_generator').async_generator

    return [i async for i in async_generator()]
