"""
Exercism Problem 2: Leap
"""

def is_leap_year(year):
    """Return True if the year is a leap year"""

    if year % 4 == 0:
        if not year % 100 == 0:
            return True

        if year % 100 == 0 and year % 400 == 0:
            return True

    return False
