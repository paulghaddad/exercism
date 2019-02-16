from string import ascii_lowercase as lower, ascii_uppercase as upper

def rotate(text, key):
    key = key % 26
    rotated_lower = lower[key:] + lower[:key]
    rotated_upper = upper[key:] + upper[:key]

    rotation_mapping = str.maketrans(lower+upper, rotated_lower + rotated_upper)
    return text.translate(rotation_mapping)
