"""
Problem 4: Remove Duplicates In-place ⭐⭐

Without using extra space, remove duplicates from a sorted array.

Return the new length.

Example

Input

[1,1,2,2,3,3,3,4]

Output

4

Modified array

[1,2,3,4,...]
"""

arr = [1,1,2,2,3,3,3,4]

j = 1

for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        arr[j] = arr[i]
        j += 1

print(j)
print(arr[:j])