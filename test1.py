import pytest


def add(x, y):
    return x + y


def test_method():
    assert add(4, 5) == 9
