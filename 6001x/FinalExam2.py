def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    # Your code here
    primes = []
    for i in range(2, N+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes
