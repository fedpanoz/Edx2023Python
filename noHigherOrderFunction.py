L = [1, 2, 3, 4]
def general_poly(L):
    L = L[::-1]
    def inner(x):
        result = 0
        for i in range(len(L)):
            result += L[i] * x ** i
        return result
    return inner
print(general_poly([1, 2, 3, 4])(10))
