# Create a mapping (try using zip) and then translate that to a string

def rotate_char(char, key):
    if char.isupper():
        baseline = ord('A')
        new_value = (ord(char) + key - baseline) % 26 + baseline
    elif char.islower():
        baseline = ord('a')
        new_value = (ord(char) + key - baseline) % 26 + baseline
    else:
        new_value = ord(char)

    return chr(new_value)

def rotate(text, key):
    rotated_text = ''

    for char in text:
      rotated_text += rotate_char(char, key)

    return rotated_text
