people = ['Mauricio', 'Sara', 'Eurice']
print(people[0])
print(people[1])
print(people[2])

collection = ['Mauricio', False, 1.0, 13, [1, 2, 3]]
print(collection[0])
print(collection[4])
print(collection)

## Strings can be indexed like lists
message = 'Hello, World!'
print(message[4])

## Lists can be added and multiplied like strings
nums1 = [1, 2, 3]
nums2 = [4, 5]
nums = nums1 + nums2
print(nums)
print(nums1 * 2)

## The in operator can be used to check if an element is inside a list
print(1 in nums1)
print(1111 in nums1)

## It also can be used to verify if a string contains a substring
print("ello" in "Hello, World!")

## Not in can also be used
print(1111 not in nums1)
print('w' not in 'abcdef')