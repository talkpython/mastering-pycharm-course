# App 7: Wizard Battle App

![image](app-7-screenshot.png)
 
If you want to try this yourself, try to build the interactive app above. 

This application will is a Dungeons and Dragons / MUD style text-based role playing game involving wizards and creatures.

Key concepts introduced
=================

**Classes**

    class Creature:
        def fight(self, opponent):
            if self.level > opponent.level:
                # fight
            else:
                # fleet
       
        def rest(self):
            # rest logic

**Initializers and Fields**

    class Creature:
    
        def __init__(self, name, level):
             self.name = name
             self.level = level
             self.modifier = random.randint(5, 12)

**Magic methods**

    class Creature:
    
        def __init__(self, name, level):
             # controls initialization
             
        def __str__(self):
             # defines string rep
             
        def __iter__(self, name, level):
             # allows for use in for-in loops

        def __eq__(self, other):
            # behavior for the equality operator, ==.
        def __ne__(self, other)
            # The inequality operator, !=.
        def __lt__(self, other)
            # the less-than operator, <.
        def __gt__(self, other)
            # the greater-than operator, >.
        def __le__(self, other)
            # the less-than-or-equal-to operator, <=.
        def __ge__(self, other)
        
        def ...

More info: [A Guide to Python's Magic Methods](https://github.com/RafeKettler/magicmethods/blob/master/magicmethods.pdf)

**Inheritance**

    class Creature:
        # ...

    class SmallAnimal(Creature):
        # ...

    class FierceFighter(Creature):
        # ...
        
    class Dragon(FierceFighter):
        # ...
        
    class Wizard(FierceFighter):
        # ...

**Polymorphism**

    # works on any type defined above that is-a creature
    
    def fight(hero, creature):
        if hero.battle(creature): ...

