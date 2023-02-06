rootToFind = float(input('Tell me number to find the root'))
low = 0
high = max(1, rootToFind)
epsilon = 0.01
numOfSteps = 0
ans = (high + low) / 2
while(abs(ans ** 2 - rootToFind) >= epsilon):
    print(f'ans is {ans}, low is {low}, high is {high}, number of steps is {numOfSteps}')
    numOfSteps += 1
    if ans ** 2 < rootToFind:
        low = ans
    else:
        high = ans

    ans = (low + high) / 2
print(f'Your square root is {ans}\n')