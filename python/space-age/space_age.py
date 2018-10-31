class SpaceAge(object):
    EARTH_YEAR_IN_SECONDS = 31557600
    RELATIVE_PLANET_YEARS_MAP = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        age = self.seconds / (
            self.RELATIVE_PLANET_YEARS_MAP["mercury"] * self.EARTH_YEAR_IN_SECONDS
        )
        return round(age, 2)

    def on_venus(self):
        age = self.seconds / (
            self.RELATIVE_PLANET_YEARS_MAP["venus"] * self.EARTH_YEAR_IN_SECONDS
        )
        return round(age, 2)

    def on_earth(self):
        age = self.seconds / (
            self.RELATIVE_PLANET_YEARS_MAP["earth"] * self.EARTH_YEAR_IN_SECONDS
        )
        return round(age, 2)

    def on_mars(self):
        age = self.seconds / (
            self.RELATIVE_PLANET_YEARS_MAP["mars"] * self.EARTH_YEAR_IN_SECONDS
        )
        return round(age, 2)

    def on_jupiter(self):
        age = self.seconds / (
            self.RELATIVE_PLANET_YEARS_MAP["jupiter"] * self.EARTH_YEAR_IN_SECONDS
        )
        return round(age, 2)

    def on_saturn(self):
        age = self.seconds / (
            self.RELATIVE_PLANET_YEARS_MAP["saturn"] * self.EARTH_YEAR_IN_SECONDS
        )
        return round(age, 2)

    def on_uranus(self):
        age = self.seconds / (
            self.RELATIVE_PLANET_YEARS_MAP["uranus"] * self.EARTH_YEAR_IN_SECONDS
        )
        return round(age, 2)

    def on_neptune(self):
        age = self.seconds / (
            self.RELATIVE_PLANET_YEARS_MAP["neptune"] * self.EARTH_YEAR_IN_SECONDS
        )
        return round(age, 2)
