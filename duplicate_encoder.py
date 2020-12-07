def duplicate_encode(word):
    return ''.join(')' if word.lower().count(i.lower())>1 else '(' for i in word)
