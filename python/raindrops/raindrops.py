FACTORS_TO_SOUNDS = {3: "Pling", 5: "Plang", 7: "Plong"}


def convert(num):
    return f"{sound(num, 3)}{sound(num, 5)}{sound(num, 7)}" or str(num)


def sound(num, factor):
    return FACTORS_TO_SOUNDS[factor] if num % factor == 0 else ""
