#!/usr/bin/env python3
"""A type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
        A float multiplier.
    Returns:
        A function that multiplies a float by multiplier
    """
    def multi(n: float) -> float:
        """multiplies a float by multiplier"""
        return float(n * multiplier)
    return multi
