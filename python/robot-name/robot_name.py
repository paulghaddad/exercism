import string
import random


class Robot(object):
    UPPERCASE_LETTERS = string.ascii_uppercase
    NUMBER_OF_LETTERS_IN_NAME = 2
    NUMBER_OF_DIGITS_IN_NAME = 3

    def __init__(self):
        self.name = self._create_random_name()


    def reset(self):
        self.name = self._create_random_name()


    def _create_random_name(self):
        name = ''
        for i in range(self.NUMBER_OF_LETTERS_IN_NAME):
            name += random.choice(self.UPPERCASE_LETTERS)

        for i in range(self.NUMBER_OF_DIGITS_IN_NAME):
            name += str(random.randint(0, 9))

        return name
