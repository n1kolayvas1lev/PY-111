from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) > 1:
        mid = len(container)//2
        L = container[:mid]
        R = container[mid:]
        sort(L)
        sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):  # Копируем данные из временных массивов.
            if L[i] < R[j]:
                container[k] = L[i]
                i += 1
            else:
                container[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            container[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            container[k] = R[j]
            k += 1
            j += 1

    return container
