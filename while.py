i = int(input())
while i < 10:
    print(i)
    i += 1
j = 0
while j < 100:
    if j == 5:
        print('breaking loop')
        break
    print(j)
    j += 1
print('end of program!')