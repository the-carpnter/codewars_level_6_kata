def locate(seq, value, i=0):
    try:
        if seq[i] == value:
            return True
    except IndexError:
        return False
    if type(seq[i]) is list:
        if locate(seq[i], value, i=0):
            return True
    return locate(seq, value, i+1)   
