def fibonacci_terc(n):
    """
    Evaluates fibonacci_terc function
    :param n: integer number
    :return: fibonacci_terc(n)
    """
    if n < 0:
        raise ValueError('Fibonacci is not defined for negative values')
    return fibonacci_terc(n - 2) + fibonacci_terc(n - 1) if n >= 2 else n if n > 0 else 0