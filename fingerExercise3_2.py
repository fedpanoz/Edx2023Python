integer = int(input("Enter an integer: "))

found = False
for pwr in range(2, 6):
    root = int(integer**(1/pwr))
    if root**pwr == integer:
        print("root:", root)
        print("pwr:", pwr)
        found = True
        break

if not found:
    print("No such pair of integers exists")