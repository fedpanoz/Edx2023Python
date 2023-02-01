primesSum = 0
for numX in range(3, 1001, 2):
    for divisor in range(3, numX):
        if numX % divisor == 0:
            break
    else:
        print(f'{numX}\n')
        primesSum += numX
        print(f'La somma è :{primesSum}')