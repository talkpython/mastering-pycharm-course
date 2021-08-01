from creature_base import Creature


class SmallAnimal(Creature):
    def get_defensive_roll(self, modifier=3):
        base_roll = super().get_defensive_roll(modifier)
        return base_roll / 2