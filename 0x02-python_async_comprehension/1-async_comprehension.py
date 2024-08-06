#!/usr/bin/env python3
"""
Module for collecting random numbers
using an asynchronous comprehension.
"""

import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator.

    Returns:
        A list of 10 random float numbers.
    """
    return [number async for number in async_generator()]
