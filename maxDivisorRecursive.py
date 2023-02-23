""" Write a recursive function gcdIter(a, b) that returns the greatest common divisor of a and b."""
def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
print(gcdRecur(12, 9))