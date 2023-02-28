max_calories = 0
current_calories = 0
for line in input().splitlines():
    if line.strip() == '':
        max_calories = max(max_calories, current_calories)
        current_calories = 0
    else:
        current_calories += int(line)
max_calories = max(max_calories, current_calories)

print(max_calories)
