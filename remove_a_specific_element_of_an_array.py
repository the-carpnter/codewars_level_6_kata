from functools import reduce
def select_subarray(arr):
    k = []
    min = None
    id, val = None, None
    sum = reduce(lambda x,y: x+y, arr)
    product = reduce(lambda x,y: x*y, arr)
    for i,v in enumerate(arr):
        sub_sum = sum - v
        sub_prod = product // v
        if sub_sum:
            q = abs(sub_prod/sub_sum)
            if min:
                if q < min:
                    min = q
                    id, val = i, v
                    k = []
                elif q == min:
                    k += [[id, val], [i, v]]
            else:
                min = q
                id, val = i, v
    return k if k else [id, val]  
