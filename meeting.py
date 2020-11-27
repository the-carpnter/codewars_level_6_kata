f = lambda x: tuple(map(str.upper, x.split(':')[::-1]))
def meeting(s):
    guests = s.split(';')
    names = sorted(sorted([f(guest) for guest in guests], key = lambda x: x[1]), key = lambda x: x[0])
    return ''.join('('+', '.join(name) + ')' for name in names)
