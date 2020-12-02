def comp(a1, a2):
    try:
        return sorted(map(lambda x: x**2, a1)) == sorted(a2)
    except TypeError:
        return False
