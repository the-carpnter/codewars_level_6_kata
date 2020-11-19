def is_triangle_number(x):
    if type(x) is not int:
        return False
    for i in range(0,x+1):
        if i*(i+1)/2 == x:
            return True
    return False
