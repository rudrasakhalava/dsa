arr = [1,2,2,3,3,3,4]

freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

max = 0
ans = None

for key,value in freq.items():
    if freq[value] > max:
        max = freq[value]
        ans = key

print(f"Element {ans} is most time appeared")