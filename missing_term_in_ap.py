def find_d(a):
    k = []
    i = 1
    while True:
        d = a[i] - a[i-1]
        if d in k:
            return d
        k += [d]
        
def find_missing(a):
    d = find_d(a)
    i = 0
    while True:
        if a[i+1] - a[i] != d:
            return a[i+1] - d
