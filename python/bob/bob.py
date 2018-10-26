import re


def hey(phrase):
    condensed_phrase = phrase.strip(" \t\n\r")

    is_question = condensed_phrase.endswith("?")
    is_uppercase = condensed_phrase.isupper()

    if is_question and is_uppercase:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_uppercase:
        return "Whoa, chill out!"
    elif not condensed_phrase:
        return "Fine. Be that way!"
    else:
        return "Whatever."
