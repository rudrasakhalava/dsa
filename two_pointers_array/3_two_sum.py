""" 
Problem

You are given a sorted array nums and an integer target.

Return the maximum sum of two numbers that is strictly less than target.

If no such pair exists, return -1.

Example
Input:
nums = [1,3,4,7,10]
target = 15

Output:
14

Explanation

4 + 10 = 14

It is the largest sum smaller than 15.
"""

nums = [1,3,4,7,10]
target = 15

i = 0
j = len(nums)-1

temp = -1

while i < j:
    sum = nums[i] + nums[j]

    if sum < target and sum > temp:
        temp = sum
        i += 1
    else:
        j -= 1

print(temp)        
