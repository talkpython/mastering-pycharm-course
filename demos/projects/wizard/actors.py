import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

        if self.level < 1:
            raise ValueError("level")

    def get_defensive_roll(self, modifier=3):
        roll = random.randint(1, 12)
        return modifier * roll * self.level


class Wizard(Creature):

    def fight(self, creature):
        print(f"The wizard {self.name} attacks {creature.name}!")

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print(f"You roll {my_roll:,}...")
        print(f"{creature.name} rolls {creature_roll:,}...")

        if my_roll >= creature_roll:
            print(f"The wizard has handily triumphed over {creature.name}")
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            return False

    def __repr__(self):
        return f"Wizard: {self.name} of level {self.level}"


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2

    def __repr__(self):
        return f"SmallAnimal: {self.name} of level {self.level}"


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)

        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self, modifier=3):
        base_roll = super().get_defensive_roll(modifier)
        fire_modifier = None
        if self.breaths_fire:
            fire_modifier = 5
        else:
            fire_modifier = 1
        scale_modifier = self.scaliness / 10

        return int(base_roll * fire_modifier * scale_modifier)

    def __repr__(self):
        return f"Dragon: {self.name} of level {self.level}"
