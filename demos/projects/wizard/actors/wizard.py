from creature_base import Creature


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
