#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A coroutine called async_generator that takes no arguments
    and will yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
        yield number
