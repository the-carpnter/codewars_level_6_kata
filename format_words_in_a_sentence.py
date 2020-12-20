def format_words(words):
    if not words:
        return ''
    words = [*filter(lambda x: x, words)]
    if len(words) >= 2:
        return ', '.join(words[:-1]) + ' and ' + words[-1]
    return words[0] if words else ''
