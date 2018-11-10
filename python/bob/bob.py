RESPONSES = {
    "shouting_a_question": "Calm down, I know what I'm doing!",
    "shouting": "Whoa, chill out!",
    "question": "Sure.",
    "silence": "Fine. Be that way!",
    "default": "Whatever."
}

def hey(phrase):
    normalized_phrase = phrase.strip(" \t\n\r")

    shouting = is_shouting(normalized_phrase)
    asking_question = is_question(normalized_phrase)
    shouting_question = shouting and asking_question
    silence = not normalized_phrase

    if shouting_question:
        return RESPONSES["shouting_a_question"]

    if shouting:
        return RESPONSES["shouting"]

    if asking_question:
        return RESPONSES["question"]

    if silence:
        return RESPONSES["silence"]

    return RESPONSES["default"]


def is_shouting(phrase):
    return phrase.isupper()


def is_question(phrase):
    return phrase.endswith("?")
