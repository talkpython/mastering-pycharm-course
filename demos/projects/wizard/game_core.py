import random
import time

from actors.creature_base import Creature
from actors.small_animal import SmallAnimal
from actors.dragon import Dragon
from actors.wizard import Wizard

STARTING_HERO_LEVEL = 75


def game_loop():
    creatures = []
    creatures.append(SmallAnimal('Toad', 1))
    creatures.append(Creature('Tiger', 12))
    creatures.append(SmallAnimal('Bat', 3))
    creatures.append(Dragon('Dragon', 50, 75, True))
    creatures.append(Wizard('Evil Wizard', 1000))

    hero = Wizard('Gandolf', STARTING_HERO_LEVEL)
    # print(f"REPR: {creatures[-2]}")

    while True:

        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appear from a dark and foggy forest...')
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.fight(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print(f'The wizard {hero.name} takes in the surroundings and sees:')
            for c in creatures:
                print(f' * A {c.name} of level {c.level}')
        else:
            print("OK, exiting game... bye!")
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()
