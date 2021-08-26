# Your turn: Projects

## Objectives

1. Create a new project and run it
2. Open and configure an existing (semi) complex project

## Create a new project

To create a new project, use PyCharm's new project wizard. 

Steps:

1. Open PyCharm
2. Create a new project
3. Name it first_project and use a virtual environment (see image below)
4. Uncheck "create main.py script"
5. Add a hello.py
6. Print *hello world*
7. Run within PyCharm (right-click on `hello.py` in the project window and choose `Run 'hello'`)
8. Verify that the virtual environment's version of Python was used (see Python path in the second image below)

![Create project with venv](./resources/virtualenv.png)

![Run with venv python](./resources/hello.png)

## Configure a complex project

In this section, you'll check out the Python Jumpstart by Building 10 Apps demo content. Just clone it from the repository here:

[https://github.com/talkpython/python-jumpstart-course-demos](https://github.com/talkpython/python-jumpstart-course-demos)

```shell
$ git clone https://github.com/talkpython/python-jumpstart-course-demos
```

If you don't _git_, that's OK. Just download and unzip it (click the `code` button then download as zip).

Open `python-jumpstart-course-demos` as a project in PyCharm. Just choose `File > Open` and browse to the file.
If you're on macOS, you can also drag-and-drop the folder onto the PyCharm icon in the dock.

PyCharm may show a warning that there is "No interpreter configured" for the project. If that's the case,
click the interpreter section in the lower right, chose `Add interpreter`, then `New environment`.

You will want to configure the wizard battle section to work correctly with the relative imports. Mark this directory as a **sources root**:

`./apps/07_wizard_battle/final/`

Then configure PyCharm to run `program.py` in that folder.

You should also have no errors around this statement in the PyCharm editor.

	# program.py, line 4
	from actors import Wizard, Creature, SmallAnimal, Dragon

Run it and enjoy your wizard battle. Good luck with the dragon!

![Configured (no errors) and running](./resources/config-run.png)

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/mastering-pycharm-course/issues) or fix it and [submit a PR](https://github.com/talkpython/mastering-pycharm-course/pulls).*
