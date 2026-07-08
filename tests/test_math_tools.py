from scripts.math_tools import add, is_even


def test_adds_two_numbers():
    assert add(2, 3) == 5


def test_detects_even_number():
    assert is_even(4) is True


def test_detects_odd_number():
    assert is_even(5) is False

