SHOUTING_A_QUESTION = "Calm down, I know what I'm doing!"
SHOUTING = "Whoa, chill out!"
QUESTION = "Sure."
SILENCE = "Fine. Be that way!"
DEFAULT = "Whatever."

def hey(phrase):
    normalized_phrase = phrase.strip(" \t\n\r")

    shouting = is_shouting(normalized_phrase)
    question = is_question(normalized_phrase)
    shouting_a_question = shouting and question
    silence = not normalized_phrase

    if shouting_a_question:
        return SHOUTING_A_QUESTION

    if shouting:
        return SHOUTING

    if question:
        return QUESTION

    if silence:
        return SILENCE

    return DEFAULT


def is_shouting(phrase):
    return phrase.isupper()


def is_question(phrase):
    return phrase.endswith("?")
