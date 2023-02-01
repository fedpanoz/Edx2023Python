i = 0
lista_nums = []
while i < 10:
    numx = int(input("Tell me a number please: \n"))
    if numx % 2 != 0:
        lista_nums.append(numx)
    i += 1
if lista_nums:
    print(max(lista_nums))
else:
    print('i am sorry i have found no odd numbers\n')

