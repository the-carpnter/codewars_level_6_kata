def sum_arrays(a,b):
    if not a and not b: return []
    x = int(str(abs(a[0])) + ''.join(map(str, a[1:]))) * [1,-1][a[0] < 0] if a else 0
    y = int(str(abs(b[0])) + ''.join(map(str, b[1:]))) * [1,-1][b[0] < 0] if b else 0
    z = [*map(int, str(abs(x+y)))]
    return [z[0]*-1] + z[1:] if x + y < 0 else z
