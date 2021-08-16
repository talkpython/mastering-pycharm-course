import random


def test_hello_pytest():
    assert 1 > 0


def test_change_to_fail():
    num = random.randint(100, 200)
    assert num < 201
