def Xbonacci(sig,n):
    fib = sig.copy()
    while True:
        x = sum(sig)
        fib += [x]
        sig = sig[1:] + [x]
        if len(fib) >= n:
            break
    return fib[:n]  
