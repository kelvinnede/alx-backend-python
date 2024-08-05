#!/usr/bin/env python3
"""
This module contains a function that returns an asyncio.Task
"""

import asyncio
from typing import Any
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine
    with the given max_delay.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: The created asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
