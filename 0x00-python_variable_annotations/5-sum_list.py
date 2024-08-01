#!/usr/bin/env python3
"""
This module contains a function that sums a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of float numbers and return the result.

    Args:
        input_list (List[float]): The list of float numbers.

    Returns:
        float: The sum of the float numbers in the list.
    """
    return sum(input_list)
