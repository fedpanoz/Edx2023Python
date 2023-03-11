"""
Write a lambda expression that has two numeric parameters.If the second argument equals zero, it should return None.
otherwise it should return the value of dividing the first argument by the second argument.
Hint: use a conditional expression.
"""

print((lambda x, y: x/y if y != 0 else None)(5, 3))
print((lambda x, y: x/y if y != 0 else None)(5, 0))
result = (lambda x, y: x/y if y != 0 else None)(5, 98)
print(result)



