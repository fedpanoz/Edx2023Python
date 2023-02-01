numX = int(input('Gimme an integer please:\n'))
for pwr in range(2, 6):
    root = numX ** (1 / pwr)
    if root ** pwr == numX:
        print(f'Your root is {root}, your power is {pwr}')
        break
else:
    print('I am sorry there are no such ints.')