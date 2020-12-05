def weird_word(word):
    k = ''
    for i,c in enumerate(word):
        if i%2==0:
            k += c.upper()
        else:
            k += c.lower()
    return k
            
def to_weird_case(string):
    return ' '.join(map(weird_word, string.split()))
