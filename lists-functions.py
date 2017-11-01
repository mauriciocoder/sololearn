cars = ['Fiesta', 'CRV', 'TT']
cars.append('C4')
print(cars)
print(len(cars))
cars.insert(1, 'Fox')
print(cars)
print(cars.index('CRV'))

print('#### Another operations ####')
'''
There are a few more useful functions and methods for lists.
max(list): Returns the list item with the maximum value
min(list): Returns the list item with minimum value
list.count(obj): Returns a count of how many times an item occurs in a list
list.remove(obj): Removes an object from a list
list.reverse(): Reverses objects in a list
'''
print(max(cars))

## It is possible to create a range also
nums = list(range(10))
print(nums)

## You can also set the starting value of range
nums = list(range(3, 10))
print(nums)
print(range(10) == range(0, 10))

## You can also set the increment ratio
print(list(range(0, 100, 10)))