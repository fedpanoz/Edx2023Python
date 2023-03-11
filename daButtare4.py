prova = [1, -2, 3.4, 45]
def applyToEach(L, f):
    for x in range(len(L)):
        L[x] = f(L[x])
    return L
print(applyToEach(prova, int))