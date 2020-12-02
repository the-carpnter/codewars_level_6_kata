def count_bits(n):
    count = 0
    while n:
        n, m = divmod(n, 2)
        count += m==1
    return count
