arr = [5, 9, 2, 17, 8]

max = float("-inf")
s_max = float("-inf")

for i in arr:
    if i > max:
        s_max = max
        max = i
    elif i > s_max and i != max:
        s_max = i

print("Second Largest :: ",s_max)
print("Largest :: ",max)