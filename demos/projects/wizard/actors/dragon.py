from actors.creature_base import Creature


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)

        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self, modifier=3):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        # Another sourcery example:
        # is_strong = base_roll or 'Not strong'
        # print(is_strong)

        return int(base_roll * fire_modifier * scale_modifier)
