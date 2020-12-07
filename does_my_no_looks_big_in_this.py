def narcissistic(value):
    n = len(str(value))
    return sum(int(i)**n for i in str(value)) == value
