#!/usr/bin/env python3
"""
This module contains a function that executes multiple asynchronous
coroutines concurrently and returns their results in ascending order.
"""

import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
