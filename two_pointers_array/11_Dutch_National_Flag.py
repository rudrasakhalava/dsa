"""
 Given an array containing items of three distinct values (usually represented as 0s, 1s, and 2s, mirroring 
 the red, white, and blue of the Dutch flag), the goal is to sort the array in-place using a single pass

 Objective and ConstraintsThe primary requirement is to arrange the elements so that 
 all 0s come first, followed by all 1s, and finally all 2s.Time Complexity: O(n) 
 
 — The array must be sorted in a single linear scan.Space Complexity: O(1)
 — The operation must be done in-place, meaning no additional arrays or memory structures can be allocated.

 

 soln ->  here we use three points

 0 - low-1 -> 0's 
 low - mid-1 -> 1's 
 high - n-1 -> 2's 

                0 0 0 0 1 1 1 1 2 2 2 2
 initially ::   |       |     | |     |  
              low,mid   |     | |   high
                        |     | |____
 after ::               |     |      |
                      low   high    mid

 """
arr = [0,1,2,0,2,0,1,2,2,1,0,1]

low = 0
mid = 0
high = len(arr)-1

while mid <= high:
    if arr[mid] == 0:
        arr[mid], arr[low] = arr[low], arr[mid]
        mid += 1
        low += 1
    if arr[mid] == 1:
        mid += 1
    if arr[mid] == 2:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print(arr)