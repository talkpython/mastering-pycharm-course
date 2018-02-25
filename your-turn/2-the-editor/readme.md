# Your turn: Editor

## Objectives

1. Add a feature to a class
2. Clean up code to match PEP8
3. Remove unused imports
4. Add documentation to a method

## Add a feature to a class

Let's start exploring some of my favorite editor features in one shot. Autocomplete & constructive code intentions.

Open the project called `bad_wizard` (same folder as this file).  Creating a virtual environment in `bad_wizard` before opening it is encouraged but not technically required.

There is a lot wrong with bad wizard, but don't mess with the warnings yet. Instead, on line 43 in the file `program.py`, type 

    hero.

And observe the autocomplete. Pretty cool right?

Now let's add a method. Type this:

    hero.wake_up()

Notice that wake_up should have some warning about it not existing. Put your cursor on wake_up, press **alt-enter**, and choose "*Add method wake_up to Wizard class*".

Then write some kind of print statement for the implementation (e.g. The wizard Gandolf awakens) based on the wizard's name.

## Clean up code to match PEP8

Return to `program.py`. Notice how many PEP8 formatting warnings it has. Use reformat code to fix this!

If you forgot the command sequence, use the search (upper right) and type `reformat code`. It should appear under the "actions" section.

## Remove unused imports

Go to the top of `program.py`. You'll see some of the imports are unused. Put your cursor in that area. You should have a light bulb for a code intention. Choose "*Optimize imports*"

## Add documentation to a method

The bad wizard has no documentation. Put your cursor on `hero.attack` (the attack part) on line 57 in `program.py`. Use the menu **View > Quick Documentation** and notice it's lacking.

Press **cmd/ctrl-b** (or **cmd/ctrl-click**) to navigate to attack. Type """[ENTER] to generate documentation.

Return to line 57 in `program.py` and see your improved docs.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/mastering-pycharm-course/issues) or fix it and [submit a PR](https://github.com/talkpython/mastering-pycharm-course/pulls).*