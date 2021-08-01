import random
import time

from actors import SmallAnimal, Creature, Dragon, Wizard

STARTING_PLAYER_LEVEL = 75


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000)
    ]

    player = Wizard('Gandolf', STARTING_PLAYER_LEVEL)
    # print(f"REPR: {creatures[-2]}")

    while True:

        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appear from a dark and foggy forest...')
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if player.fight(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print(f'The wizard {player.name} takes in the surroundings and sees:')
            for c in creatures:
                print(f' * A {c.name} of level {c.level}')
        else:
            print("OK, exiting game... bye!")
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()
