#!/usr/bin/env python3
"""
This module contains a function that takes a string and an int or float,
and returns a tuple with the string and the square of the int/float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and an int/float, with the int/float squared.

    Args:
        k (str): The string to include in the tuple.
        v (Union[int, float]): The value to square and include in the tuple.

    Returns:
        Tuple[str, float]: Ttuple where the first element is the string and
        second element is the square of the int/float.
    """
    return (k, float(v ** 2))
