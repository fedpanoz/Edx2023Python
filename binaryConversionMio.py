num_x = int(input('Gimme a number to convert in binary'))
binary = ''
if num_x < 0:
    isNeg = True
    num_x = abs(num_x)
else:
    isNeg = False
if num_x == 0:
    binary = '0'
while num_x > 0:
    binary += str(num_x % 2)
    num_x = num_x // 2
if isNeg == True:
    binary = '-' + binary
binary = binary[::-1]
print(binary)