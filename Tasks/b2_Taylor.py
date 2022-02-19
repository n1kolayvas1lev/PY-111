"""
Taylor series
"""
import math
from itertools import count
from typing import Union

EPSILON = 0.00000001


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    def get_items(n):
        return x ** n / math.factorial(n)
    sum_ = 1
    for i in count(1, 1):
        cur_item = get_items(i)
        sum_ += cur_item

        if cur_item < EPSILON:
            break
    return sum_


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sum_ = 0
    for i in count(1, 1):
        current_item = get_item(x, i)
        sum_ += current_item
        if abs(current_item) <= EPSILON:
            return sum_
    # sum_ = 0
    # for i in count(1, 1):
    #     cur_item = get_item(x, i)
    #     sum_ += cur_item
    #     if cur_item <= EPSILON:
    #         return sum_


def get_item(x, n):
    # return ((-1) ** (n - 1) * x ** (2 * n - 1)) / math.factorial(2 * n - 1)
    return ((-1) ** (n - 1) * x ** (2 * n - 1)) / math.factorial(2 * n - 1)


value = 45 * math.pi / 180
print(sinx(value))


