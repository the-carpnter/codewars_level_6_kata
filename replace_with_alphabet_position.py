def alphabet_position(text):
    return ' '.join(map(str,[ord(x.lower())-96 for x in text if x.isalpha()]))
