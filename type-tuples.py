'''
Tuples are very similar to lists, except that they are immutable (they cannot be changed).
Also, they are created using parentheses, rather than square brackets.
'''

cars = ('Fiesta', 'BMW', 'Audi')
print(cars[0])
try:
    cars[3] = 'New'
except TypeError:
    print('TypeError raised, cannot assign a value to a tuple')

print('It can also be created without parentheses:')
people = 'Mauricio', 'Sara', 'Eurice'
print(people)