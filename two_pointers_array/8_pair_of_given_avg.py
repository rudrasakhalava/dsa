"""
Problem 1: Pair with Given Average ⭐

Given a sorted array and a number avg, determine whether there exists a pair whose average is exactly avg.

Example
Input:
nums = [1,2,3,4,5,6]
avg = 4

Output:
True

Because

(2 + 6) / 2 = 4

Expected Complexity:

O(n)
"""

nums = [1,2,3,4,5,6]
avg = 4

i = 0
j = len(nums)-1

a = 0

while i < j:
    a = (nums[i] + nums[j]) / 2

    if a == avg:
        print(f"{i}th and {j}th index element -> ({nums[i],nums[j]})")
        break
    
    elif a < avg :
        i += 1
    else :
        j -= 1
