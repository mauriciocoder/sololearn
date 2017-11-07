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

## You can slice a list
values = [1, 2, 3, 4]
print(values[1:3])  ## Fixed limit
print(values[1:])  ## From 1 to end
print(values[:2])  ## From start to 2

## You can also set a step
print(values[::2])
print(values[::3])

## When negative values are used for the first and second values in a slice (or a normal index), they count from the end of the list.
print(values[:-1])

## When the step is negative, you are reversing the list
print(values[::-1])

## You can create lists using list comprehension
nums = [i * 2 for i in range(10)]
print(nums)

## You can also set a condition to enforce the comprehension
nums = [i * 2 for i in range(10) if i % 2 == 0]
print(nums)



