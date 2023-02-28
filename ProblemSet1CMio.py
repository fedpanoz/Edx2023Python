# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

s = 'azcbobobegghakl'
longestSubstr = ''
for i in range(len(s)):
    newSubstr = s[i]
    for y in range((i + 1), len(s)):
        if s[y] >= s[y - 1]:
            newSubstr += s[y]
        else:
            break
    if len(newSubstr) >= len(longestSubstr):
        longestSubstr = newSubstr
print(longestSubstr)