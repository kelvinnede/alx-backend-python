#!/usr/bin/env python3
"""
This module contains a function to zoom in on an array
by repeating its elements.
"""

from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Zooms in on an array by repeating its elements.

    Args:
        lst (List[int]): The list of integers to zoom in on.
        factor (int, optional): The number of times each element
        should be repeated. Defaults to 2.

    Returns:
        List[int]: A list with the elements repeated according to the factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


# Test the function
array = [12, 72, 91]

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
