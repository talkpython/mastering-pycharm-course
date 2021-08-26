# Your turn: Editor

## Objectives

1. Add a feature to a class
2. Clean up code to match PEP8
3. Remove unused imports
4. Add documentation to a method

## Add a feature to a class

Let's start exploring some of my favorite editor features in one shot. Autocomplete & constructive code intentions.

Open the project called `bad_wizard` (same folder as this file).  Remember to create a virtual environment if 
PyCharm indicates "No interpreter selected" using PyCharm's `Add interpreter...` feature.

There is a lot wrong with `bad_wizard`, but don't mess with the warnings yet. 
Instead, on line 43 in the file `program.py`, type 

```python
    hero.
```

And observe the autocomplete, especially when hitting the period. Pretty cool right?

Now let's add a method. Type this, ignoring that it doesn't appear in autocomplete - it will:

```python
    hero.wake_up()
```

Notice that wake_up should have some warning about it not existing. Put your cursor on wake_up, 
press **alt-enter**, and choose "*Add method wake_up() to class Wizard*".

Then write some kind of print statement for the implementation (e.g. The wizard Gandolf awakens) 
based on the wizard's name. Run the app again and see your method's output in the run window.

## Clean up code to match PEP8

Return to `program.py`. Notice how many PEP8 formatting warnings it has. Use reformat code to fix this!

If you forgot the command sequence, use the search (upper right) and type `reformat code`. 
It should appear under the "actions" section. _Ah_, much better to look at now, isn't it?

## Remove unused imports

Go to the top of `program.py`. You'll see some imports are unused. Put your cursor on one of the 
unused imports (gray). You should have a light bulb for a code intention. Choose `Optimize imports`.

## Add documentation to a method

The bad wizard has no documentation. Put your cursor on `hero.attack` (the attack part) on line 58 in 
`program.py`. Use the menu **View > Quick Documentation** and notice it's lacking.

Press **cmd/ctrl-b** (or **cmd/ctrl-click**) to navigate to attack. Type """[ENTER] to generate documentation.

Return to line 58 in `program.py` and see your improved docs.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/mastering-pycharm-course/issues) or fix it and [submit a PR](https://github.com/talkpython/mastering-pycharm-course/pulls).*