"""
Write a function called general_poly, that meets the specifications below. For example, general_poly([1, 2, 3, 4])(10)
should evaluate to 1234 because
"""
def general_poly(L):
    def inner(x):
        result = 0
        for i in range(len(L)):
            result += L[i] * x ** i
        return result
    return inner
general_poly([1, 2, 3, 4])(10)
print(general_poly([1, 2, 3, 4])(10))
