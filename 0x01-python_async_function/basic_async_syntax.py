#!/usr/bin/env python3
"""
This module contains a function that waits for a random delay
and returns the delay.
"""

import asyncio
import random
from typing import Any


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay
    seconds and returns the delay.

    Args:
        max_delay (int, optional): The maximum number
        of seconds to wait. Defaults to 10.

    Returns:
        float: The number of seconds the function waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
