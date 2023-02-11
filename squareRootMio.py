# Returns the square root of a given number
numToSquare = int(input('Tell me a number you want to square\n'))
epsilon = 0.01
low = 0
high = max(1, numToSquare)
guess = 0
if numToSquare < 0:
    print(f'i am sorry {numToSquare}has no square roots')
else:
    while abs(guess ** 2 - numToSquare) > epsilon:
        if guess ** 2 > numToSquare:
            high = guess
        else:
            low = guess
        guess = (high + low) / 2
print(f'Your square root is: {round(guess)}')