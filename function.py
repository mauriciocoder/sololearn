def fibonacci(n):
    if n >= 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
    elif n >= 0:
        return n


def fibonacci_terc(n):
    """
    evaluate fibonacci_terc function using terciary conditional
    """
    return fibonacci(n - 1) + fibonacci(n - 2) if n >= 2 else (n if n >= 0 else 0)


def xfunc(num):
    if num >= 0:
        return True
    else:
        return 'less than zero'


def fibonacci_of_double(num, fib_function):
    return fib_function(num * 2)


print(fibonacci(8))
print(fibonacci_terc(8))
print(xfunc(-1))
print(fibonacci_of_double(4, fibonacci_terc))
