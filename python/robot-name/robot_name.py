import string
import random


class Robot(object):
    def __init__(self):
        self.name = self._create_random_name()


    def reset(self):
        self.name = self._create_random_name()


    def _create_random_name(self):
        letters = string.ascii_uppercase

        name = ''
        for i in range(2):
            name += random.choice(letters)

        for i in range(3):
            name += str(random.randint(0, 9))

        return name
