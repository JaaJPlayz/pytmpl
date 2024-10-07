import pytest


def test_example():
    assert 1 == 1


def test_should_fail():
    with pytest.raises(AssertionError):
        assert 1 == 2
