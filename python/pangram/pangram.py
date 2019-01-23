from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    letters_in_sentence = set(char for char in sentence.lower() if char in lowercase_letters)

    return set(lowercase_letters).issubset(letters_in_sentence)
