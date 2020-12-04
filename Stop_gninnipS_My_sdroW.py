f = lambda x: x[::-1] if len(x) >= 5 else x
def spin_words(sentence):
    return ' '.join([f(word) for word in sentence.split()])
