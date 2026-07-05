"""
Given an integer array nums, return an array where

answer[i] = product of all elements except nums[i]

You cannot use division.

Input:
[1,2,3,4]

Output:
[24,12,8,6]
"""

arr = [1,2,3,4]
arr2 = []

for i in range(len(arr)):
    mul = 1
    for j in arr:
        if j != arr[i]:
            mul *= j
    arr2.append(mul)

print(arr2)