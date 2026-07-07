"""
Problem 4: Four Sum (Medium-Hard)
Problem

Given an integer array nums and an integer target.

Return all unique quadruplets whose sum equals the target.

The answer should not contain duplicate quadruplets.

Example

Input

nums = [1,0,-1,0,-2,2]
target = 0

Output

[
[-2,-1,1,2],
[-2,0,0,2],
[-1,0,0,1]
]
"""

nums = [1,0,-1,0,-2,2]
nums.sort()
target = 0

ans = []

for i in range(len(nums)-3):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    for j in range(i+1,len(nums)-2):
        if j > 1 and nums[j] == nums[j-1]:
            continue
        k = j+1
        l = len(nums)-1

        while k < l:
            sum = nums[i] + nums[j] + nums[k] + nums[l]

            if sum == target:
                ans.append([nums[i] , nums[j] , nums[k] , nums[l]])
                k += 1
                l -= 1

                if nums[k] == nums[k-1]:
                    k += 1
                if nums[l] == nums[l+1]:
                    l -= 1
            
            elif sum > target :
                l -= 1
            
            else :
                k += 1

print(ans)