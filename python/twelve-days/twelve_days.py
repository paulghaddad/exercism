DAY_PHRASE_MAPPING = {
    1: "first"
}

DAY_VERSE_MAPPING = {
    1: "a Partridge in a Pear Tree"

}

def recite(start_verse, end_verse):
    day_phrase = DAY_PHRASE_MAPPING[end_verse]
    verse = DAY_VERSE_MAPPING[start_verse]


    return [
        f"On the {day_phrase} day of Christmas my true love gave to me: " +
        verse +
        "."
    ]
