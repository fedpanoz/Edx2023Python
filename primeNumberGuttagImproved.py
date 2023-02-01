x = int(input("i tell you if it is a prime:\n"))
minDivisor = 0
ans = 0
if x % 2 == 0:
    minDivisor = 2
else:
    for guess in range(3, x, 2):
        if x % guess == 0:
            minDivisor = guess
            break

    if minDivisor == 0:
        print(f'{x} is a fucking Prime')
    else:
        print(f'The min divisor is :{minDivisor}')

