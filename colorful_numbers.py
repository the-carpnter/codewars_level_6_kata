def colorful(number):
    n = str(number)
    a = [*map(int, n)]+[int(x)*int(y) for x,y in zip(n, n[1:])]
    return len(a) == len(set(a))
