# Your turn: Unit testing

## Objectives

1. Configure purest tests
2. Use code coverage to see how much test coverage you have

## Configure pytest tests

We'll start with an existing project in this folder: `yourtable`.

Create a virtual environment and open it in PyCharm.

To run the tests, you'll need to add a pytest run configuration. In the run configurations, pull it down and choose 'edit'. Then add a new one:

![](./resources/add.png)

Set the target to `path` with value `./tests.py`. Now run the tests and see they are failing.

![](./resources/failing.png)
