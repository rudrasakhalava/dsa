"""
Problem

Given a string s, return the first character that appears exactly once. If none exists, return -1.

Input:
"leetcode"

Output:
'l'
Input:
"aabbcc"

Output:
-1
"""
s = input("Enter the string :: ")

freq = {}

for i in s:
    if i in freq:
        freq[i] += 1
    else :
        freq[i] = 1 

for j in freq:
    if freq[j] == 1:
        print(j)
        break
else :
    print(-1)