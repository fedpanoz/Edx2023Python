""" Write a iterative function gcdIter(a, b) that returns the greatest common divisor of a and b."""
def gcdIter(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(gcdIter(272, 306))