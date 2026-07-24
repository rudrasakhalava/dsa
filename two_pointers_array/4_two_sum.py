""" 
Problem 2: Count Pairs Smaller Than Target (Easy-Medium)
Problem

Given a sorted array nums and an integer target.

Count how many pairs (i, j) satisfy

i < j
nums[i] + nums[j] < target

Example

Input

nums = [1,2,3,4,5]
target = 7

Output

6

Explanation

Pairs are

(1,2)
(1,3)
(1,4)
(1,5)
(2,3)
(2,4)

Constraint

O(n)
"""

nums = [1,2,3,4,5]
target = 7

i = 0
j = len(nums)-1

temp = 0

while i < j:
    sum = nums[i] + nums[j]

    if sum < target:
        temp += (j-i)
        i += 1
    elif sum >= target :
        j -= 1

print(temp)