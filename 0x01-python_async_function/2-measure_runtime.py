#!/usr/bin/env python3
"""measures the total execution time"""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)

    Parameters:
    -----------
    n (int): Number of times to call wait_n.
    max_delay (int): Maximum delay for each call to wait_n.

    Returns:
    --------
    float: Average execution time per call to wait_n.
    """
    start = time()
    run(wait_n(n, max_delay))
    end = time()
    return (end - start) / n
