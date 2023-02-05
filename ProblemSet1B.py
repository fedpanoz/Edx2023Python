'''Count how many times in string s occurs the substriing 'bob'''''
s = 'azcbobobegghakl'
substring = 'bob'
count = 0

for i in range(len(s) - len(substring) + 1):
    if s[i:i+len(substring)] == substring:
        count += 1

print("Number of times bob occurs is:", count)