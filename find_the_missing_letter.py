def find_missing_letter(chars):
    a = [ord(i) for i in chars]
    k = range(min(a), max(a)+1)
    for i in k:
        if i not in a:
            return chr(i)
