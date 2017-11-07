## Formatting by index substitution
cars = ['BMW', 'Audi', 'Ferrari']
print('You can find in store, cars: {0}, {1}, {2}'.format(cars[0], cars[1], cars[2]))

## Formatting by variable substitution
boy = 'Mauricio'
girl = 'Sara'
my_age = 31
print(f'I have a {cars[0]}')
print(f'My name is {boy} and my age is {my_age} and my fiancee is {girl}')
print(f'My name is {boy} and my fiancee is {girl}'.format(boy=boy, girl=girl))
