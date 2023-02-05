def egg_drop(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 4:
        return 4
    elif n == 5:
        return 5
    elif n == 6:
        return 6
    elif n == 7:
        return 7
    else:
        return egg_drop(n-1) + egg_drop(n-2) + egg_drop(n-3) + egg_drop(n-4) + egg_drop(n-5) + egg_drop(n-6) + egg_drop(n-7)

print(egg_drop(30))
