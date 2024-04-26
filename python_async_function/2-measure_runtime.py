#!/usr/bin/env python3
"""
A measure_time function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay), and returns
total_time / n.
"""
import asyncio
import time
from typing import List


wait_import = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the average time for wait_n(n, max_delay)
    """
    start = time.perf_counter()
    asyncio.run(wait_import(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
