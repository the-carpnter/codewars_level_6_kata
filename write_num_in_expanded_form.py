def expanded_form(n):
    k = []
    while n:
        n, m = divmod(n,10)
        k += [m]
    return ' + '.join(map(str,[x*10**i for i,x in enumerate(k) if x][::-1]))
