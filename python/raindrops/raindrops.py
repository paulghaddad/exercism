FACTORS_TO_SOUNDS = {
    3: "Pling",
    5: "Plang",
    7: "Plong",
}


def convert(number):
    output = ""

    if number % 3 == 0:
        output += FACTORS_TO_SOUNDS[3]

    if number % 5 == 0:
        output += FACTORS_TO_SOUNDS[5]

    if number % 7 == 0:
        output += FACTORS_TO_SOUNDS[7]

    return output or str(number)
