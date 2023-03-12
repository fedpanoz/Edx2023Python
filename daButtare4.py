prova = [1, -2, 3.4, -45]
# def applyToEach(L, f):
#     for x in range(len(L)):
#         L[x] = f(L[x])
#     return L
# print(applyToEach(prova, int))
# acca = map(abs, prova)
# print(acca)
# print(type(acca))
# for x in acca:
#     print(x)
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a * a

def halve(a):
    return a / 2

def inc(a):
    return a + 1
