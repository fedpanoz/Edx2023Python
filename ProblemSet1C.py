# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

s = 'azcbobobegghakl'

max_substring = ""
current_substring = ""
for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        current_substring += s[i]
    else:
        current_substring += s[i]
        if len(current_substring) > len(max_substring):
            max_substring = current_substring
        current_substring = ""

print("Longest substring in alphabetical order is: " + max_substring)