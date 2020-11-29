from gmpy2 import next_prime
def only_oddDigPrimes(n):
    x = next_prime(0)
    k = []
    while True:
        if set(str(x)) <= set('13579'):
            k += [x]
            if x > n:
                return [len(k)-1, k[-2], k[-1]]
        x = next_prime(x)
