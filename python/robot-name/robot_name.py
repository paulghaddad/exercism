import random
from string import (
    ascii_uppercase as uppercase_letters,
    digits
)


class Robot(object):
    NUMBER_OF_LETTERS_IN_NAME = 2
    NUMBER_OF_DIGITS_IN_NAME = 3

    def __init__(self):
        self.name = self.__class__.create_random_name()


    def reset(self):
        self.name = self.__class__.create_random_name()

    @classmethod
    def create_random_name(cls):
        # Use join to create a random name

        name = ''
        for i in range(Robot.NUMBER_OF_LETTERS_IN_NAME):
            name += random.choice(uppercase_letters)

        for i in range(Robot.NUMBER_OF_DIGITS_IN_NAME):
            name += random.choice(digits)

        return name
