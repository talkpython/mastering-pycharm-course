# Your turn: Debugging

## Objectives

1. Create breakpoints
2. Use the visual debugger to understand code flow
3. Alter the flow with the debugger

We will use the project called `math_tricks` in the same folder as this file. You won't need to write any code but will just understand and alter values while running.

Open `math_tricks` in PyCharm.

If you run `program.py`, you should see:

```python
[1, 1, 3, 5, 13, 21, 55, 89, 233, 377, 987]
```

## Create breakpoints

We are going to explore what is happening when we iterate over `odd_fibs`. Set a breakpoint on this line:

```python
if o > 1000:
```

## Use the visual debugger to understand code flow

Run the app in the debugger. You should see the execution stop on this line.

Use step in, over, out and the variable state views (variables windows and editor overlays) to navigate through this series of code until you get the zen of generator methods.

## Alter the flow with the debugger

Let's make something happen to test an additional case not naturally found in our execution.

Convert the breakpoint to a conditional one with the condition being `o > 1000`.

Now restart the app in the debugger. You should be stopped with `o = 1,597`.

Our goal is to make the loop run one more time. In the variables window, set `o` to `999`. Now let the program run to completion. You should see the unnatural output with 999 in our Fibonacci set:

```python
[1, 1, 3, 5, 13, 21, 55, 89, 233, 377, 987, 999]
```

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/mastering-pycharm-course/issues) or fix it and [submit a PR](https://github.com/talkpython/mastering-pycharm-course/pulls).*
