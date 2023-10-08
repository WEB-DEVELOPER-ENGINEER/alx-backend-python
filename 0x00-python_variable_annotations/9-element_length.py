#!/usr/bin/env python3
"""calculate the length of each element within an iterable of sequences and
return the results as a list of tuples"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.
    Return:
        List[Tuple[Sequence, int]]: A list of tuples.
    """
    return [(i, len(i)) for i in lst]
