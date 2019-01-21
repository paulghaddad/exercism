def rotate(text, key):
    rotated_text = ''

    for letter in text:
        if letter.isupper():
            baseline = ord('A')
            new_value = (ord(letter) + key - baseline) % 26 + baseline
        elif letter.islower():
            baseline = ord('a')
            new_value = (ord(letter) + key - baseline) % 26 + baseline
        else:
            new_value = ord(letter)

        rotated_text += chr(new_value)


    return rotated_text
