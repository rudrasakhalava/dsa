arr = [-2, 4, 0, 6, -7, 8, 0]

zero = 0
n = 0
p = 0

for i in arr:
    if i == 0:
        zero += 1
    elif i < 0:
        n += 1
    elif i > 0:
        p += 1

print("Zeros :: ",zero)
print("-ves :: ",n)
print("+ves :: ",p)