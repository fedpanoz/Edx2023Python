"""
Write a function that accepts either one or two ints as arguments.If called with two arguments, the function prints
the product ot the two arguments.If called with one argument, it prints that argument
"""
def product(x, y=1):  # y=1 is the default value
    return x * y
print(product(2, 3))
print(product(2))
#

