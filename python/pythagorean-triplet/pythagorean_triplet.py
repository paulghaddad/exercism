def triplets_with_sum(number):
    triplets = set()

    for c in range(1, number):
        for b in range(1, c):
            for a in range(1, b):
                if a < b and b < c:
                    if a**2 + b**2 == c**2:
                        if a + b + c == number:
                            triplets.add((a, b, c))

    return triplets



def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    pass
