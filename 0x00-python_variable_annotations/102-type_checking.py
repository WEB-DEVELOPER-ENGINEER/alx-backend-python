#!/usr/bin/env python3
"""Defines a Python function called zoom_array that takes a tuple of elements
and a zoom factor as input. It returns a new list where each element from
the input tuple is repeated according to the zoom factor."""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom Array"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
