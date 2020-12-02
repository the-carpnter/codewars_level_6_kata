import string

def is_pangram(s):
    return set(i.lower() for i in s if i.isalpha()) == set(string.ascii_lowercase)
