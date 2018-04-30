# Your turn: Performance

## Version warning

This chapter requires PyCharm Professional to complete as indicated. Please see the [chart for version breakdown](https://training.talkpython.fm/courses/explore_pycharm/mastering-pycharm-ide#editions) in the public course page.

## Objectives

1. Understand an existing app's performance
2. Improve a few key methods performance  

## Understand an existing app's performance

In this *your turn*, we'll be exploring an existing app's performance. Open the project called `perf_app` in this folder.

Note that you will need to install `requests` for it to run.

Create a run configuration by right-clicking on `program.py` and choosing 'run'. It should run, but slowly.

Now with the run configuration in place, you can profile it.

![](./resources/profile.png)

Use the various tools in PyCharm's reporting to answer: What the the three slowest methods and why?

## Improve a few key methods performance  

Now that you understand the performance, make changes to the code to improve the speed (there are a few TODO comments in the code). Use profiling to verify this is actually improving things and by how much.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/mastering-pycharm-course/issues) or fix it and [submit a PR](https://github.com/talkpython/mastering-pycharm-course/pulls).*