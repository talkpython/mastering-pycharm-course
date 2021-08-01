import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

        if self.level < 1:
            raise ValueError("level")

    def get_defensive_roll(self, modifier=3):
        die_roll = random.randint(1, 12)

        return modifier * die_roll * self.level

    def __repr__(self):
        return f"{type(self).__name__}: {self.name} of level {self.level}"
