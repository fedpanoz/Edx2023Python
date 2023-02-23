x = float(input('Gimme a number to convert in binary'))
binary = ''
p = 0
while((2 ** p) * x) % 1 != 0:
    p += 1
num = int(x * 2 ** p)
while num > 0:
    binary += str(num % 2)
    num //= 2
print(binary)
newBina = '0' * p + binary
print(newBina)