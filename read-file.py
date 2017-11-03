filename = 'test-files/file-test'
file = open(filename, 'r')
content = file.read()
file.close()
print('content = {}'.format(content))

## print only part in bytes of file
file = open(filename, 'r')
content_of_20_bytes = file.read(20)
print(content_of_20_bytes)
content_of_20_bytes = file.read(20)
print(content_of_20_bytes)
file.close()

## once a file have already been read and not closed, it wont bring any content at all!
file = open(filename)
content = file.read()
print(content)
content = file.read()
assert len(content) == 0
file.close()

## we can also get all lines of file
file = open(filename, 'r')
lines = file.readlines()
print(lines)
file.close()

## or you can iterate on array
file = open(filename, 'r')
for line in file:
    print(line.strip())
file.close()

## you can work with a file, without having to worry about not closing it
with open(filename) as file:
    print('Printing without having to close!!!')
    print(file.read())

