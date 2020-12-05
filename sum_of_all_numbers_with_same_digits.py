def fact(n):
    re = 1
    for i in range(1, n+1):
        re = re*i
    return re

def sum_arrangements(num):
    l = len(str(num))
    return fact(l-1)*sum(map(int, str(num)))*int('1'*l)
