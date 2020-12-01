def tribonacci(sig, n):
    a, b, c = sig
    k = [a, b, c]
    while True:
        if len(k) > n:
            return k[:n]
        a, b, c = b, c, a+b+c
        k += [c]
