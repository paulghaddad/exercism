from __future__ import division


class Rational(object):

    @staticmethod
    def calculate_gcd(numer, denom):
        greatest_number = max(numer, denom)

        for i in range(greatest_number, 0, -1):
            if numer % i == 0 and denom % i == 0:
                return i

        return 1


    def __init__(self, numer, denom):
        gcd = self.calculate_gcd(numer, denom)

        if numer > 0 and denom < 0:
            numer *= -1
            denom *= -1
        elif numer < 0 and denom < 0:
            numer *= -1
            denom *= -1

        self.numer = int(numer / gcd)
        self.denom = int(denom / gcd)


    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom


    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)


    def __add__(self, other):
        numer = self.numer * other.denom + self.denom * other.numer
        denom = self.denom * other.denom

        if numer == 0:
            denom = 1

        return Rational(numer, denom)


    def __sub__(self, other):
        numer = self.numer * other.denom - self.denom * other.numer
        denom = self.denom * other.denom

        if numer == 0:
            denom = 1

        return Rational(numer, denom)


    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom

        return Rational(numer, denom)


    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = other.numer * self.denom

        return Rational(numer, denom)


    def __abs__(self):
        if self.denom < 0 and self.numer < 0:
            return Rational(self.numer * -1, self.denom * -1)
        elif self.numer < 0:
            return Rational(self.numer * -1, self.denom)
        elif self.denom < 0:
            return Rational(self.numer, self.denom* -1)
        else:
            return Rational(self.numer, self.denom)


    def __pow__(self, power):
        numer = self.numer ** power
        denom = self.denom ** power

        return Rational(numer, denom)


    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
