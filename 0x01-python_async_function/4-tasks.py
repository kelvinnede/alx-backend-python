#!/usr/bin/env python3
"""
This module contains a function that executes multiple asynchronous
tasks concurrently and returns their results in ascending order.
"""

import asyncio
from typing import List
from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple task_wait_random coroutines concurrently.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
