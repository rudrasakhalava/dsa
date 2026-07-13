"""
Merge Two Sorted Arrays 

Without using extra sorting.

Input

arr1 = [1,4,7]
arr2 = [2,3,6]

Output

[1,2,3,4,6,7]

"""

arr1 = [1,4,7]
arr2 = [2,3,6]

arr = []

i = 0
j = 0

while i <= len(arr1)-1 and i <= len(arr1)-1:
    if arr1[i] <= arr2[j]:
        arr.append(arr1[i])
        arr.append(arr2[j])
        
    else :
        arr.append(arr2[j])
        arr.append(arr1[i])

    i += 1
    j += 1 

print(arr)   
