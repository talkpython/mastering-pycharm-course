# Your turn: Source control

## Objectives

1. Use **git** from within PyCharm
2. Use local history as an orthogonal, local source control 


## `git` from within PyCharm

We are going to create a very simple game and store it in source control.

In this chapter, you will need to have [git](https://github.com/git-guides/#what-is-git) installed. 
Our friends over at GitHub have created a nice 
[Installing git on any OS guide](https://github.com/git-guides/install-git). If you don't have git or are
unsure whether you do, please check out the steps for your OS [over there](https://github.com/git-guides/install-git).

## Keeping it simple

While most work like this will be done with a cloud source control services such as 
[GitHub](https://github.com), [BitBucket](https://bitbucket.org/), or [GitLab](https://about.gitlab.com/),
we won't go to that trouble here. We will just create a local **git** repository using these steps:

1. Simply create directory called `hilo` in the terminal / command prompt
2. CD into `hilo`
3. Create a local **git** repo by typing `git init`

This `hilo` directory is now a local **git** repo (it has a hidden `.git` folder).

Time to **write some code**:

* Open this directory in PyCharm (it's empty but will constitute a new project)
* If PyCharm creates a default `main.py`, just delete it
* Confirm that PyCharm has detected the **git** / vcs root (see the default branch name in the lower right status bar fork icon)
* Create a file named `game.py`. 
* Tell PyCharm it may add `game.py` and all subsequent files to **git** if asked (i.e. "don't ask again").
* Write a quick game that will generate the output below. You'll need a `while` loop, `random.randint()`, and some `if` and `print` statements.  
* While writing this game, save often (cmd/ctrl-s). This is important for [step 2](#local-history).

 **Sample game output**
 
```
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
```

Time to **check in your code**:

Use the menu `Git > Commit` to commit your `game.py` file. Notice how the color of game.py changes from 
green to white after committed. Choose a nice commit message.

## Local history

Now let's see what's in **local history**.

Right-click on `game.py` in the project. Choose `local history > show history`. 
Click around on the left of the local history window and you should see several versions of your file 
(regardless of whether they were committed to git).

*See a mistake in these instructions? Please 
[submit a new issue](https://github.com/talkpython/mastering-pycharm-course/issues) or fix it and 
[submit a PR](https://github.com/talkpython/mastering-pycharm-course/pulls).*