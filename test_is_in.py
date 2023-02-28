"""Write a function test_is_in to test the function is_in(string1, string2) that accepts two strings as arguments and
 return True
if either string occurs anywhere in the other, and False otherwise"""
import pytest
from twoStrings import is_in
def test_is_in():
    if is_in('hello', 'world') == True:

        print('Test 1 passed')
    else:
        print('Test 1 failed')
    if is_in('hello', 'brid hello caiazzo') == False:
        print('Test 2 passed')
    else:
        print('Test 2 failed')
    if is_in('hello', 'hello') == True:
        print('Test 3 passed')
    else:
        print('Test 3 failed')
    if is_in('hello', 'world') == False:
        print('Test 4 passed')
    else:
        print('Test 4 failed')
    if is_in('hello', 'world') == True:
        print('Test 5 passed')
    else:
        print('Test 5 failed')
    if is_in('hello', 'world') == False:
        print('Test 6 passed')
    else:
        print('Test 6 failed')
    if is_in('hello', 'world') == True:
        print('Test 7 passed')
    else:
        print('Test 7 failed')
    if is_in('hello', 'world') == False:
        print('Test 8 passed')
    else:
        print('Test 8 failed')
    if is_in('hello', 'world') == True:
        print('Test 9 passed')
    else:
        print('Test 9 failed')
    if is_in('hello', 'world') == False:
        print('Test 10 passed')
    else:
        print('Test 10 failed')
    if is_in('hello', 'world') == True:
        print('Test 11 passed')
    else:
        print('Test 11 failed')
    if is_in('hello', 'world') == False:
        print('Test 12 passed')
    else:
        print('Test 12 failed')
    if is_in('hello', 'world') == True:
        print('Test 13 passed')
    else:
        print('Test 13 failed')
    if is_in('hello', 'world') == False:
        print('Test 14 passed')
    else:
        print('Test 14 failed')
    if is_in('hello', 'world') == True:
        print('Test 15 passed')
    else:
        print('Test 15 failed')
    if is_in('hello', 'world') == False:
        print('Test 16 passed')


