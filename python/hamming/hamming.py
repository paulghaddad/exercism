from functools import reduce


def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The strands are not the same length.")

    return reduce(lambda p, c: p + 1 if c[0] != c[1] else p, zip(strand_a, strand_b), 0)
