def fib(n, a = 0, b = 1):
    if n < 0:
        return None
    if n:
        return fib(n-1, b, a+b)
    return a

def fib_seq(n):
    i = 0
    while True:
        if fib(i) > n:
            break
        i += 1  
    return [fib(x) for x in range(i)]

def Zeckendorf_rep(n):
    if n == 0:
        return []
    if n < 0:
        return None
    ar = fib_seq(n)
    k = [ar[-1]]
    for i in ar[1:-1][::-1]:
        if sum(k) + i <= n:
            k += [i]
    return k   
