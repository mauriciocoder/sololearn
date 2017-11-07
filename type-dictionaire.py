print('2) Dictionaries are equivalent to Java Map')
wallets = {1210: 'Mauricio', 1211: 'Sara'}
print(wallets[1210])
print(wallets[1211])
try:
    person = wallets[2]
except KeyError:
    print('index not present raises a KeyError!')

print('2.1) Dictionaires key is not mutable')
v = 'BMW'
prices = {'Volvo': 200000, v: 100000}
v = 'Audi'
print(prices['BMW'])  ## It still prints 100000

print('2.2) You can put another values in a dictionaire')
prices['Fiesta'] = 13000
print(prices['Fiesta'])

print('2.3) You can check if a dictionaire contains a key')
if ('Fiesta' in prices):
    print('Fiesta is in prices!')
if ('Ferrari' not in prices):
    print('Ferrari not in prices!')

print('2.4) You can also use get to retrieve a value')
print(prices.get('Fiesta'))
