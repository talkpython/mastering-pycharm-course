# Your turn: Source control

## Objectives

1. Use git from within PyCharm
2. Use local history as an orthogonal source control 


## `git` from within PyCharm

We are going to create a very simple game and store it in source control.

If you have a GitHub account, feel free to create a repository named `hilo` there, clone it, and use it for this purpose. 

If you don't want to make a public repo, then:

1. simply create directory called `hilo`
2. Cd into `hilo`
3. Create a local git repo by typing `git init`

Now this `hilo` directory has a local git repo (either from the result of cloning or via init). 

While you're here, add a virtual environment named `.env` in `hilo`.

Time to **write some code**.

* Open this directory in PyCharm
* Confirm with PyCharm that you want to add the git / vcs root when prompted
* Create a file `game.py`, tell PyCharm it may add it and all subsequent files to git if asked.
* Write a quick game that will generate the output below. You'll need a `while` loop, `random.randint()`, and some `if` and `print` lines.  
* While writing this game, save often (cmd/ctrl-s).

 **Sample game output**
 
		Welcome to the HI - LO game
		Guess a number between 1 & 100: 50
		Too low!
		Guess a number between 1 & 100: 75
		Too high!
		Guess a number between 1 & 100: 65
		Too low!
		Guess a number between 1 & 100: 70
		Too high!
		Guess a number between 1 & 100: 68
		Too high!
		Guess a number between 1 & 100: 67
		Too high!
		Guess a number between 1 & 100: 66
		Got it: The number is 66
  
Time to **check in your code**.

Use the menu VCS > Commit to commit your game.py file. Notice how the color of game.py changes from green to white after committed.

If you made a github repo, feel free to push your commit as well.

## Local history

Now let's see what's in **local history**.

Right-click on `game.py` in the project. Choose **local history > show history**. Click around on the left of the local history window and you should see several versions of your file (regardless of whether they were committed to git).

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/mastering-pycharm-course/issues) or fix it and [submit a PR](https://github.com/talkpython/mastering-pycharm-course/pulls).*