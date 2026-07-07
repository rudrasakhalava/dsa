"""
Problem 3: Three Sum Closest (Medium)
Problem

Given an integer array nums and an integer target.

Find three integers whose sum is closest to target.

Return the sum.

Example

Input

nums = [-1,2,1,-4]
target = 1

Output

2

Explanation

(-1 + 2 + 1) = 2

Difference is only 1.

"""

nums = [-1,2,1,-4]
nums.sort()
target = 1

dif = 0

for i in range(len(nums)-2):
    j = i + 1
    k = len(nums)-1

    while j < k :
        sum = nums[i] + nums[j] + nums[k]