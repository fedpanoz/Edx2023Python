prova = [1, -2, 3.4, -45]
# def applyToEach(L, f):
#     for x in range(len(L)):
#         L[x] = f(L[x])
#     return L
# print(applyToEach(prova, int))
acca = map(abs, prova)
print(acca)
print(type(acca))
for x in acca:
    print(x)