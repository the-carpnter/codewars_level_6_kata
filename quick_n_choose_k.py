def choose(n,k, accum = 1, denom = 1):
    if k:
        return choose(n-1, k-1, accum*n, denom*k)
    return accum//denom
