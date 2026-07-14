from calendar_utils import is_leap_year

def test_not_multiple_of_4():
    assert is_leap_year(2000) is True  # RED: is_leap_year doesn't exist yet