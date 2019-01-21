from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    chars_in_sentence = [char for char in sentence.lower() if char in lowercase_letters]
    letters_in_sentence = ''.join(chars_in_sentence)

    return set(letters_in_sentence) == set(lowercase_letters)
