""" Wrtite an implementation of of fibonacci sequence using a dictionary."""
def fibonacciWithDictionary(n, dictionary):
    if n in dictionary:
        return dictionary[n]
    else:
        ans = fibonacciWithDictionary(n-1, dictionary) + fibonacciWithDictionary(n-2, dictionary)
        dictionary[n] = ans
        return ans
    

d = {1:1, 2:2}
print(fibonacciWithDictionary(10, d))
