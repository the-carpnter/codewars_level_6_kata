from itertools import product
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2==0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def prime_primes(n):
    sum = 0
    count = 0
    for x,y in product(filter(is_prime,range(1,n)), repeat = 2):
        if x < y:
            count += 1
            sum += (x/y)
    return count, int(sum)
