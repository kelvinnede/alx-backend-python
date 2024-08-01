#!/usr/bin/env python3
"""
This module contains a function that safely retrieves a
value from a dictionary with a default fallback.
"""

from typing import Mapping, Any, Union, TypeVar

# Define a type variable
T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Retrieves the value associated with a key from a dictionary
    or returns a default value if the key is not found.

    Args:
        dct (Mapping[Any, T]): A dictionary-like object.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): The value to return
        if the key is not found. Defaults to None.

    Returns:
        Union[T, None]: The value associated with the key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
