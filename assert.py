"""
An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
An expression is tested, and if the result comes up false, an exception is raised.
Assertions are carried out through use of the assert statement.
"""


def assert_positive(n):
    assert n > 0


def assert_positive_2(n):
    assert n > 0, f'Can only accept positive numbers, n = {n}'


## assert_positive(-1)
assert_positive_2(-1)
