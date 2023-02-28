# Count how many times in string s occurs the substring 'bob'
s = 'azcbobobegghakl'
subStr = 'bob'
count = 0
for i in range(len(s)):
    if s[i:(i + 3)] == 'bob':
        count += 1
print(count)
