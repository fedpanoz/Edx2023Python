xToFindSquare = float(input('Tell me a number you want to approximatly square'))
epsilonApprox = 0.00001
ans = 0
step = epsilonApprox ** 2
numOfGuesses = 0
while(abs(ans ** 2 - xToFindSquare) >= epsilonApprox and ans <= xToFindSquare):
    ans += step
    numOfGuesses += 1
print(f'The number of guesses is {numOfGuesses}')
if abs(ans ** 2 - xToFindSquare) < epsilonApprox:
    print(f'Your square root is {ans} and it quitly approximates the exact root')

else:
    print('i am sorry i did not find a valid root')