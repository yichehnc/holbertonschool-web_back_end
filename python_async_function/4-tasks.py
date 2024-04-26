#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of delays in ascending order
    """
    delays: List[float] = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    return sorted(delays)
