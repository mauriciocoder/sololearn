## Class definition with methods and attributes
class Car:
    def __init__(self, name, engine):
        self.name = name
        self.engine = engine

    def run(self):
        print(self)
        if self.engine > 3.0:
            print('Wwwrooooooommmm!!!!')
        elif self.engine > 2.0:
            print('Rrrroooooommmmm!!!!')
        else:
            print('Powpowpowpowpow!!!!')


c1 = Car('Fiesta', 1.0)
c2 = Car('Ferrari', 4.0)
print(c1.engine)
c1.run()
c2.run()


## Class with static attribute
class Dog:
    legs = 4

d = Dog()
print(d.legs)
print(Dog.legs)
try:
    d.doStuff()
except AttributeError:
    print('You have tried to invoke an undefined method!')
try:
    d.head
except AttributeError:
    print('You have tried to invoke an undefined attribute!')


# Class using inheritance
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'{self.name} {self.salary}'

class Manager(Employee):
    def __init__(self, name, salary, teams):
        super().__init__(name, salary)
        self.teams = teams

    def __str__(self):
        return super().__str__() + f' {self.teams}'

class Analyst(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team

    def __str__(self):
        return super().__str__() + f' {self.team}'


e1 = Analyst('Mauricio', 8800, 'balcao')
e2 = Manager('Clay', 15000, {'balcao', 'td'})
print(e1)
print(e2)


## There is also some magic methods used to oveload operators
'''
More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'<{self.x}, {self.y}>'

v1 = Vector(10, 10)
v2 = Vector(5, 5)
v3 = v1 + v2
print(v3)

## There are class methods (static methods that receives cls)
## and static methods

class Rectangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def __str__(self):
        return f'{self.length}, {self.height}'

    @classmethod
    def build(cls, length, height):
        return cls(length, height)

    @staticmethod
    def build_static(length, height):
        return Rectangle(length, height)


r = Rectangle.build(10, 20)
print(r)
r = Rectangle.build_static(10, 20)
print(r)


## In Python a member is either public or private (starts with __ and ends with none)
class Pet:
    def __init__(self, name):
        self.__name = name

p = Pet('Luke')
try:
    print(p.__name)
except AttributeError:
    print('AttributeError thrown')

