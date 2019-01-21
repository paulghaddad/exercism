import string


def is_pangram(sentence):
    chars_in_sentence = [char for char in sentence.lower() if char in string.ascii_lowercase]
    letters_in_sentence = ''.join(chars_in_sentence)

    return set(letters_in_sentence) == set(string.ascii_lowercase)
