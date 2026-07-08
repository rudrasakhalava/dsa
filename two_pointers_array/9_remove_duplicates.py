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

i = 1

while i < len(arr):
    if arr[i] == arr[i-1]:
        arr.pop(i)
    else :
        i += 1

print(len(arr))
print(arr)