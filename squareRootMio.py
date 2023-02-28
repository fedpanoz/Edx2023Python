# Calculate the square root of a given number by the bisection algorithm
squareToFind = int(input('Gimme an int to find its square root'))
epsilon = 0.01
guess = 0
if squareToFind < 0:
    print('i am sorry there is no square roots for negative numbers')
else:
    low = 0
    high = max(1, squareToFind)
    while abs(guess ** 2 - squareToFind) >= epsilon:
        if guess ** 2 > squareToFind:
            high = guess
        else:
            low = guess
        guess = (high + low) / 2

print(f'Your square root is {guess}')