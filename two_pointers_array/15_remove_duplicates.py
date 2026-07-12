"""

Remove Duplicates from Sorted Array 

Problem

Given a sorted array, remove duplicates in-place and return the number of unique elements.

Example

Input:
[1,1,2,2,3,4,4]

Output:
4

Modified array:
[1,2,3,4]

"""

arr = [1,1,2,2,3,4,4]

l = 0

for r in range(1,len(arr)):
    if arr[l] != arr[r]:
        l += 1
        arr[l] = arr[r]

print(arr)