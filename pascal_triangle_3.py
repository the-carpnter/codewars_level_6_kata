from itertools import chain
def pascals_triangle(n):
    p = [[1], [1,1], [1,2,1], [1,3,3,1]]
    while len(p) <= n:
        x = [1]+[sum(p[-1][i:i+2]) for i in range(len(p)-1)]+[1]
        p+=[x]
    return [*chain(*p[:n])]
