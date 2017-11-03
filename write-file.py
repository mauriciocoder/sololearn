filename = 'test-files/file-test'
try:
    file = open(filename, 'w')
    # the content is cleared!
    message = 'python is CAKE!'
    bytes_saved = file.write(message)
    assert len(message) == bytes_saved
finally:
    file.close()