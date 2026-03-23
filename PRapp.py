import pytest
from PR1 import example

def test_1():
    assert example(2, 3) == 23
    assert example(1, 3) == 13
    assert example(0, 3) == 6

