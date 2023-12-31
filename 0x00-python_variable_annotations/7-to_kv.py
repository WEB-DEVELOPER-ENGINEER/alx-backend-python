#!/usr/bin/env python3
"""type-annotated function to_kv that takes a string k and an int OR float v
as arguments and returns a tuple. The first element of the tuple is the string
k. The second element is the square of the int/float v."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        A string k and an int OR float v.
    Returns:
        A tuple of two elements:
            The first element the string k.
            The second element is the square of the int/float v.
    """
    return (k, v**2)
