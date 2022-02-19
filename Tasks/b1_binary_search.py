from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    # min_index = 0
    # max_index = len(arr) - 1
    # while max_index >= min_index:
    #     middle_index = (max_index + min_index) // 2
    #     value = arr[middle_index]
    #     if value == elem:
    #         return middle_index
    #     if value > elem:
    #         max_index = middle_index - 1
    #     if value < elem:
    #         min_index = middle_index + 1
    # return None
    if len(arr) < 10:
        return arr.index(elem)
    sorted_array = sorted(arr)
    right_border = len(sorted_array) - 1
    left_border = 0
    if left_border > right_border:
        return None
    while left_border <= right_border:
        middle = (right_border + left_border) // 2
        if sorted_array[middle] == elem:
            return middle
        elif sorted_array[middle] < elem:
            left_border = middle + 1
        elif sorted_array[middle] > elem:
            right_border = middle - 1
        else:
            return None


if __name__ == "__main__":
    binary_search(5, [i for i in range(100)] + [101])
