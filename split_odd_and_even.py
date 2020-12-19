def split_odd_and_even(n):
    n = list(str(n))
    cache = n[0]
    k = []
    for i, d in enumerate(n[1:], 1):
        if int(n[i])%2 == int(n[i-1])%2:
            cache += d
        else:
            k += [cache]
            cache = d
    k += [cache]
    return [*map(int,k)]
