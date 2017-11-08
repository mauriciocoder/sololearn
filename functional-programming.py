## lambda are anonymous functions. Rule: lambda {parameters} : {single_expression}

def my_print(func, value):
    print('This is my_print {}'.format(func(value)))

my_print(lambda x : x * 2, 2)

## You can also create and call the lambda
print((lambda x : x * 2)(4))

## You can set a variable for later use
double = lambda x : x * 2
print(double(4) + double(2))

## You can pass two other values for lambda
sum = lambda x, y : x + y
print(sum(3, 4))

## $$$$$ Maps

def addOne(n):
    return n + 1

nums = [1, 2, 3]
print(list(map(addOne, nums)))

## You can receive a lambda also
print(list(map(lambda n : n + 1, nums)))

## $$$$$ Filter
print(list(filter(lambda n : n % 2 > 0, nums)))


## $$$$$ Generator -> With generators you can create a stream of objects

def count(nums):
    for num in range(nums):
        yield num

for n in count(10):
    print(n)

def concat(text):
    result = ''
    for ch in text:
        result += ch
        yield result

print(list(concat('adaba')))