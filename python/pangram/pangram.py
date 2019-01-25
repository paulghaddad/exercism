from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    # Approach 1: Are all the letters from a-z in the sentence
    return set(lowercase_letters).issubset(sentence.lower())

    # Approach 2: Is every letter in a-z in the sentence
    return set(sentence.lower()).issuperset(lowercase_letters)
