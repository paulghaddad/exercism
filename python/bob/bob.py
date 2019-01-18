def hey(phrase):
    return (
        forceful_question(phrase) and "Calm down, I know what I'm doing!" or
        question(phrase) and "Sure." or
        yelling(phrase) and "Whoa, chill out!" or
        silence(phrase) and "Fine. Be that way!" or
        "Whatever."
    )


def question(phrase):
    return phrase.rstrip().endswith("?")


def yelling(phrase):
    return phrase.isupper()


def forceful_question(phrase):
    return question(phrase) and yelling(phrase)


def silence(phrase):
    return not phrase.strip()
