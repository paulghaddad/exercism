def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The strands are not the same length.")

    difference = 0

    for position, letter_1 in enumerate(strand_a):
        if letter_1 != strand_b[position]:
            difference += 1

    return difference

