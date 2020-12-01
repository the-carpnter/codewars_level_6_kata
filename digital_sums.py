def digital_root(n):
    if n == 0:
        return 0
    return n%9 if n%9 else 9
