import re


class SpaceAge(object):
    EARTH_YEAR_IN_SECONDS = 31557600
    ORBITAL_PERIODS = {
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


    def _relative_earth_years_for_planet(self, planet):
        age = self.seconds / (
            self.ORBITAL_PERIODS[planet] * self.EARTH_YEAR_IN_SECONDS
        )
        return round(age, 2)


    def __getattr__(self, name):
        planet_name = re.search(r'(?<=on_)\w+', name).group(0)
        planet_func = lambda name=planet_name: self._relative_earth_years_for_planet(name)
        setattr(self, name, planet_func)
        return getattr(self, name)
