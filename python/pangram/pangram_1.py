from string import ascii_lowercase as a_z

"""
Complexity: Unsure, depends on implementation of set operations in Python
"""


def is_pangram(sentence):
    if not sentence:
        return False

    letters_in_sentence = set(sentence.lower())
    return set(letters_in_sentence).issuperset(set(a_z))
