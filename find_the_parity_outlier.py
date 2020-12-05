def find_outlier(integers):
    parity = [i%2 for i in integers]
    if parity.count(1) > parity.count(0):
        return integers[parity.index(0)]
    return integers[parity.index(1)]
