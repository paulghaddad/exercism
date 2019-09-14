DAY_PHRASE_MAPPING = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
}

DAY_CLAUSE_MAPPING = {
    1: "a Partridge in a Pear Tree",
    2: "two Turtle Doves",
    3: "three French Hens",
    4: "four Calling Birds",
    5: "five Gold Rings",
    6: "six Geese-a-Laying",
    7: "seven Swans-a-Swimming",
    8: "eight Maids-a-Milking",
    9: "nine Ladies Dancing",
    10: "ten Lords-a-Leaping",
    11: "eleven Pipers Piping",
    12: "twelve Drummers Drumming",
}

def recite(start_verse, end_verse):
    return [construct_verse(i) for i in range(start_verse, end_verse + 1)]


def construct_verse(verse_number):
    day_phrase = DAY_PHRASE_MAPPING[verse_number]

    initial_phrase = f"On the {day_phrase} day of Christmas my true love gave to me: "
    verse_clauses = _construct_verse_clauses(verse_number)

    return initial_phrase + verse_clauses

def _construct_verse_clauses(verse_number):
    verse_clauses = ""

    for verse_number in range(verse_number, 0, -1):
        verse_clause = DAY_CLAUSE_MAPPING[verse_number]

        verse_clauses += f"{verse_clause}"

        if verse_number > 2:
            verse_clauses += ", "
        elif verse_number == 2:
            verse_clauses += ", and "
        else:
            verse_clauses += "."

    return verse_clauses
