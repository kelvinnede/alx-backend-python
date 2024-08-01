#!/usr/bin/env python3
"""
This module contains a function that sums a mixed list of integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum a list of integers and float numbers and return the result as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and float numbers.

    Returns:
        float: The sum of the numbers in the list as a float.
    """
    return sum(mxd_lst)
