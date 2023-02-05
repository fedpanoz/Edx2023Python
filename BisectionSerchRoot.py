numX = float(input('Tell me a float and i find its root with bisection search'))
numOfattempts = 0
epsilon = 0.01
high = max(1, numX)
low = 0
ans = (high + low) / 2
while abs(ans ** 2 - numX) >= epsilon:
    if ans ** 2 > numX:
        high = ans
    else:
        low = ans
    ans = (high + low) / 2
    numOfattempts += 1
    print(f'your root is {ans} and the numbers of attempts are {numOfattempts}')




