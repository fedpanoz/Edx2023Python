def rucurSum(n):
    if n == 1:
        return 1
    else:
        return n + rucurSum(n-1)
print(rucurSum(6))