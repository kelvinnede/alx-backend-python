#!/usr/bin/env python3
"""
Module for measuring the runtime of parallel async comprehensions.
"""

import asyncio
import time
from typing import List
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times in parallel.

    Returns:
        The total runtime as a float.
    """
    start_time = time.time()

    tasks = [
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    ]

    await asyncio.gather(*tasks)

    end_time = time.time()
    return end_time - start_time
