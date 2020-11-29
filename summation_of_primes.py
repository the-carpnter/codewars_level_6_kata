from gmpy2 import next_prime
def summationOfPrimes(n):
    x = next_prime(0)
    sum = 0
    while True:
        if x > n:
            return sum
        sum += x
        x = next_prime(x)
