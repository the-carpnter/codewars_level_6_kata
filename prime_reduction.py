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

def prime_red(n):
    while True:
        n = sum(int(i)**2 for i in str(n))
        if n == 4:
            return False
        if n == 1:
            return True

def solve(a,b):
    count = 0
    for i in range(a,b):
        if is_prime(i):
            if prime_red(i):
                count += 1
    return count
