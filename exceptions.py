"""
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.
"""
from mymath import fibonacci

try:
    num = 10
    den = 5
    print(num / den)
except ZeroDivisionError:
    print('ZeroDivisionError')
except:
    print('Default exception, catches all!!!')
finally:
    print('Finally called!')
print('end of program')

## Example of raising exception and re-raise
try:
    fibonacci.fibonacci_terc(-10)
except ValueError:
    raise   ## re-raise

fibonacci.fibonacci_terc(-10)   ## no need for raise
