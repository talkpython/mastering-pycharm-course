import time
import random

from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    # Yes, I added this after I recorded the video,
    # but I thought you'd get a kick out if it. ;)
    print()
    print('-----------------------------------------------------------------------')
    print(r'''
   (  )   /\   _                 (
    \ |  (  \ ( \.(               )                      _____
  \  \ \  `  `   ) \             (  ___                 / _   \\
 (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
- .-               \+  ;          (  O                           \____
     WIZARD BATTLE        )        \_____________  `              \  /
(__       APP      +- .( -'.- <. - _  VVVVVVV VV V\                 \/
(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
  .    /./.+-  . .- /  +--  - .     \______________//_              \_______
  (__ ' /x  / x _/ (                                  \___'          \     /
 , x / ( '  . / .  /                                      |           \   /
    /  /  _/ /    +                                      /              \/
   '  (__/                                             /                  \\
    ''')
    print()
    print('-----------------------------------------------------------------------')
    print()


def game_loop():
    creatures = create_creates()

    # print(creatures)

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            do_attack(active_creature, creatures, hero)
        elif cmd == 'r':
            do_runaway()
        elif cmd == 'l':
            do_look_around(creatures, hero)
        else:
            do_goodbye()
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()


def create_creates():
    return [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000)
    ]


def do_goodbye():
    print("OK, exiting game... bye!")


def do_look_around(creatures, hero, emotions=('happy', 'apprehensive')):
    emotion = random.choice(emotions)

    print(f'The wizard is {emotion}')
    print(f'{hero.name} takes in the surroundings and sees:')
    for c in creatures:
        print(f' * A {c.name} of level {c.level}')


def do_runaway():
    print('The wizard has become unsure of his power and flees!!!')


def do_attack(active_creature, creatures, hero):
    if hero.attack(active_creature):
        creatures.remove(active_creature)
    else:
        print("The wizard runs and hides taking time to recover...")
        time.sleep(5)
        print("The wizard returns revitalized!")


if __name__ == '__main__':
    main()
