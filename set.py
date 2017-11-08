## Due to the way they're stored, it's faster to check whether an item is part of a set, rather than part of a list.
nums = {1, 2, 3, 4}
for num in nums:
    print(num)

print(2 in nums)
nums.add(10)
print(nums)
nums.remove(10)
print(nums)

## You can apply set operations methods (add, diference, intersection)
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b) ## intersection
print(a | b) ## union
print(a - b) ## diference
print(a ^ b) ## either set but not in both