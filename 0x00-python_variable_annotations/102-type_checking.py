#!/usr/bin/env python3
"""
This module contains a function to zoom
an array by a specified factor.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on an array by repeating each element
    by the specified factor.

    Args:
        lst (Tuple): A tuple of elements to zoom in on.
        factor (int, optional): The factor by which
        to repeat each element. Defaults to 2.

    Returns:
        List: A list containing the zoomed-in elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
