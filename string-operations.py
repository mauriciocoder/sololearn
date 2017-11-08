s = 'hello world'.upper()
print(s)

s = 'HELLO WORLD'.lower()
print(s)

print('hello world'.startswith('hell')) # prints true
print('hello world'.endswith('ld')) # prints true
print('hello world'.endswith('world')) # prints true

print('hello world'.replace('world', 'mauricio'))

cars = ['Fiesta', 'Corola', 'C4']
s = ';'.join(cars)
print(s)
print(s.split(';'))