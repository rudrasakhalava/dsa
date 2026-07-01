# Two strings are anagrams if they contain the same characters with the same frequencies.

s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print(False)
else:
    freq1 = {}

    for i in s1:
        if i in freq1:
            freq1[i] += 1
        else:
            freq1[i] = 1

    freq2 = {}

    for j in s2:
        if j in freq2:
            freq2[j] += 1
        else:
            freq2[j] = 1

if freq1 == freq2:
    print(True)
else:
    print(False)
