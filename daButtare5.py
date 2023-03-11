def mean(*numbers):
    tot = 0
    for x in numbers:
        tot += x
    return tot / len(numbers)
print(mean(4,5,6))