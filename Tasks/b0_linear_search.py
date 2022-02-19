"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    minimum = min(arr)  # O(n)
    for i in range(len(arr)):  # O(n)
        if arr[i] == minimum:
            return i
