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
        return self._relative_earth_years_for_planet("mercury")

    def on_venus(self):
        return self._relative_earth_years_for_planet("venus")

    def on_earth(self):
        return self._relative_earth_years_for_planet("earth")

    def on_mars(self):
        return self._relative_earth_years_for_planet("mars")

    def on_jupiter(self):
        return self._relative_earth_years_for_planet("jupiter")

    def on_saturn(self):
        return self._relative_earth_years_for_planet("saturn")

    def on_uranus(self):
        return self._relative_earth_years_for_planet("uranus")

    def on_neptune(self):
        return self._relative_earth_years_for_planet("neptune")

    def _relative_earth_years_for_planet(self, planet):
        age = self.seconds / (
            self.RELATIVE_PLANET_YEARS_MAP[planet] * self.EARTH_YEAR_IN_SECONDS
        )
        return round(age, 2)
