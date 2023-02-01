listOfPrimes = []
for x in range(3, 120):
    for j in range(2, x):
        if x % j == 0:
            break
    else:
        listOfPrimes.append(x)

print(listOfPrimes)

