EQUILATERAL = 1
ISOCELES = 2
SCALENE = 3


def is_equilateral(sides):
    return len(set(sides)) == EQUILATERAL and any(sides)


def is_isosceles(sides):
    return is_triangle(sides) and len(set(sides)) == ISOCELES or is_equilateral(sides)


def is_scalene(sides):
    return is_triangle(sides) and len(set(sides)) == SCALENE


def is_triangle(sides):
    return all(sides) and sum(sorted(sides)[:2]) > max(sides)
