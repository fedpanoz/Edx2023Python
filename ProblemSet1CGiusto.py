# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc'''



s = 'kyoxggekjkbhik'
main_substring = ""
for i in range(len(s)):
    new_substring = s[i]
    for j in range(i+1, len(s)):
        if s[j] >= s[j-1]:
            new_substring += s[j]
        else:
            break
    if len(new_substring) > len(main_substring):
        main_substring = new_substring
print("Longest substring in alphabetical order is: " + main_substring)
