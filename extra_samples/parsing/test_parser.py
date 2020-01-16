import pytest

from numparser import parse


def test_basic():
    result = parse('1,3')
    assert result == [1, 3]


def test_dash():
    result = parse('1-3')
    assert result == [1, 2, 3]


def test_bad():
    with pytest.raises(ValueError):
        parse('bad')
