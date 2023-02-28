"""Write a function is_in that accepts two strings as arguments and return True if either string occurs anywhere in
 the other, and False otherwise. Hint: you might want to use the built-in str operation in. For example:"""
def is_in(string1, string2):
    if string1 in string2 or string2 in string1:
        return True
    else:
        return False
print(is_in('hello', 'helloworld'))

