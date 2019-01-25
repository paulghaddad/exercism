from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    return set(lowercase_letters).issubset(sentence.lower())
