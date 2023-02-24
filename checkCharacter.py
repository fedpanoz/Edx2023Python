""" Implement a function that takes a string alphabetically sorted and a char as inputs and returns True if char is in
 the string and False otherwise using Bisection search algorithm and recursion."""
def isIn(char, aStr):
    if aStr == "":
        return False
    elif len(aStr) == 1:
        return char == aStr
    else:
        mid = len(aStr) // 2
        if char == aStr[mid]:
            return True
        elif char < aStr[mid]:
            return isIn(char, aStr[:mid])
        else:
            return isIn(char, aStr[mid + 1:])
print(isIn('b', 'abcdefghijk'))

