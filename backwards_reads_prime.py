from gmpy2 import is_prime

def backwards_prime(start, stop):
    k = []
    for i in range(start, stop+1):
        if is_prime(i):
            n = int(str(i)[::-1])
            if is_prime(n) and str(i)!=str(i)[::-1]:
                k += [i]
    return k  
