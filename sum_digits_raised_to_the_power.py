def f(n):
    return n == sum(int(x)**i for i,x in enumerate(str(n), 1))
    
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    return [i for i in range(a, b+1) if f(i)]
