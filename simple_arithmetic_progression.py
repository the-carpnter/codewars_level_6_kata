from itertools import combinations
def solve(arr):
    k = []
    for i in combinations(arr, r =3):
        x = sorted(i)
        if x[2]-x[1] == x[1] - x[0]:
            k += [x]
    return len(k)
