from itertools import combinations
f = lambda x,y: sum(i==j for i,j in zip(x,y))
def pos_average(s):
    a = s.split(', ')
    total = 0
    re = 0
    for x,y in combinations(a, 2):
        total += len(x)
        re += f(x,y)
    print(re, total)
    return re / total * 100
