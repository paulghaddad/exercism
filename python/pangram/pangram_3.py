from string import ascii_lowercase as a_z


def is_pangram(sentence):
    letters = set(sentence.lower())
    difference = set(a_z) - letters

    return len(difference) == 0
