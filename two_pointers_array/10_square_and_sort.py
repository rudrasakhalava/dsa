"""
Problem 5: Square and Sort ⭐⭐

Given a sorted array that may contain negative numbers.

Return another sorted array containing the squares.

Example

Input

[-7,-3,-1,4,8]

Output

[1,9,16,49,64]

Expected

O(n)
"""

arr = [-7,-5,-1,4,8]

i = 0
j = len(arr)-1

res = [0] * len(arr)
position = len(arr)-1

while i <= j:
    i_square = arr[i] ** 2
    j_square = arr[j] ** 2

    if i_square > j_square:
        res[position] = i_square
        i += 1
    else :
        res[position] = j_square
        j -= 1
    position -= 1

print(res)