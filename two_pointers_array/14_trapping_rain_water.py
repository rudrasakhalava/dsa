"""

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

heights = [0,1,0,2,1,0,1,3,2,1,2,1]

l_max = 0
l = 0

r_max = 0
r = len(heights) - 1

water = 0

while l < r:

    if l_max < r_max:
        l += 1
        l_max = max(l_max,heights[l])
        water += (l_max-heights[l])

    else:
        r -= 1
        r_max = max(r_max,heights[r])
        water += (r_max-heights[r])

print(water)