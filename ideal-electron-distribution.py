def atomic_number(electrons):
    k = []
    n = 1
    while True:
        cap = 2*n*n
        e = cap if cap <= electrons else electrons
        k += [e]
        electrons = electrons - e
        n += 1
        if electrons == 0:
            return k
