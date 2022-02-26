def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    return factorial_recursive(n - 1) * n


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    f = 1
    for _ in range(1, n + 1):
        f *= _
    return f


def factorial_generator(n: int):
    if n < 0:
        raise ValueError
    f = 1
    for _ in range(0, n + 1):
        if _ == 0:
            yield f
        else:
            f *= _
            yield f


if __name__ == '__main__':
    f = factorial_generator(5)
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))

