sequence = ['a', 'b', 'c', 'a', 'b', 'a']
freq = {}
for x in sequence:
    freq[x] = freq.get(x, 0) + 1
print(freq)
