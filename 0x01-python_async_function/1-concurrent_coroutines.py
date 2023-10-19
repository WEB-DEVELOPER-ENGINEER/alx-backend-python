#!/usr/bin/env python3
"""This script provides an async routine, wait_n, that generates random delays
using the wait_random function. It spawns wait_random n times with a specified
max_delay and returns a list of all the delays in ascending order, without
using the sort() method due to concurrency considerations."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Generate a list of ascending random delays asynchronously.

    Parameters:
    -----------
    n (int): Number of delays to generate.
    max_delay (int): Maximum delay in seconds.

    Returns:
    --------
    List[float]: A list of ascending random delays.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
