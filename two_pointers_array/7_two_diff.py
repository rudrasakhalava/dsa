"""
Bonus Challenge (Original Problem)
Pair With Exact Difference (Medium)

This is a nice two-pointer problem that isn't just another sum variation.

Problem

You are given a sorted array of integers and an integer k.

Return whether there exists a pair (i, j) such that:

nums[j] - nums[i] == k

where

i < j

Example

Input

nums = [1,3,5,8,10]
k = 5

Output

True

Because

8 - 3 = 5

Example

Input

nums = [2,4,7,10]
k = 6

Output

True

Because

10 - 4 = 6

"""

nums = [2,4,7,10]
k = 5

i = 0
j = 1

while j < len(nums):
    diff = nums[j] - nums[i]

    if i == j:
        j += 1
    elif diff == k:
        print(True)
        break
    elif diff < k:
        j += 1
    else:
        i += 1
else:
    print(False)