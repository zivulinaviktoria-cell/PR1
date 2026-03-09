import pytest
from PR1 import example

def test_1():
    assert example(2, 3) == 25
    assert example(1, 3) == 16
    assert example(0, 3) == 9

