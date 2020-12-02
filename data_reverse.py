from itertools import chain
def data_reverse(data):
    k = []
    for i in range(0,len(data),8):
        k += [data[i:i+8]]
    return [i for i in chain(*k[::-1])]
