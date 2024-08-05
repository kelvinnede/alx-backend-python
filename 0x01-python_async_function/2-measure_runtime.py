#!/usr/bin/env python3
"""
This module contains a function to measure the runtime of an async function.
"""

import asyncio
import time
from typing import List
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per call.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for wait_n.

    Returns:
        float: The average execution time per call.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
