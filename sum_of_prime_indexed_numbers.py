from gmpy2 import is_prime

def total(arr):
    sum = 0
    for i, x in enumerate(arr):
        if is_prime(i):
            sum += x
    return sum
