x = int(input("i tell you if it is a prime:\n"))
maxDivisor = 0
ans = 0
minDivisor = 0
for guess in range(2, x):
    if x % guess == 0:
        minDivisor = guess
        maxDivisor = x // minDivisor
        break

if maxDivisor == 0:
    print(f'{x} is a fucking Prime')
else:
    print(f'The max divisor is :{maxDivisor}')
