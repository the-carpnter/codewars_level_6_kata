def longest_consec(a, k):
    if k > len(a):
        return ''
    if k <= 0:
        return ''
    return max([''.join(a[i:i+k]) for i in range(len(a))], key=len)
