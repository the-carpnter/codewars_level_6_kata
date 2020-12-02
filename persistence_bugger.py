def f(n):
    re = 1
    while n:
        n, m = divmod(n, 10)
        re *= m
    return re

def persistence(n):
    return 1 + persistence(f(n)) if n > 9 else 0
