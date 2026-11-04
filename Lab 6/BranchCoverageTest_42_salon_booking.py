import pytest

from salon_booking import arrival_status, can_book, extra_time_charge


@pytest.mark.parametrize(
    ("service", "duration", "stylist", "member", "expected"),
    [
        ("haircut", 30, "junior", False, 0),
        ("colour", 75, "junior", True, 0),
        ("spa", 90, "senior", True, 0),
        ("haircut", 40, "junior", False, 100),
        ("colour", 80, "senior", False, 360),
        ("haircut", 100, "junior", False, 1260),
        ("haircut", 100, "senior", False, 2100),
    ],
)
def test_extra_time_charge_branches(
    service, duration, stylist, member, expected
):
    assert extra_time_charge(service, duration, stylist, member) == expected


@pytest.mark.parametrize(
    ("service", "duration", "message"),
    [
        ("unknown", 30, "unknown service"),
        ("haircut", -1, "invalid duration"),
    ],
)
def test_extra_time_charge_validation(service, duration, message):
    with pytest.raises(ValueError, match=message):
        extra_time_charge(service, duration, "junior", False)


@pytest.mark.parametrize(
    ("party_size", "services", "walk_in", "expected"),
    [
        (2, 1, True, True),
        (3, 1, True, False),
        (5, 1, False, False),
        (4, 2, False, True),
        (4, 3, False, False),
    ],
)
def test_can_book_branches(party_size, services, walk_in, expected):
    assert can_book(party_size, services, walk_in) is expected


@pytest.mark.parametrize(
    ("minutes_early", "is_colour", "is_weekend", "expected"),
    [
        (10, False, False, "open"),
        (0, False, False, "late"),
        (-11, False, False, "closed"),
        (20, True, False, "open"),
        (10, True, True, "late"),
        (-6, True, True, "closed"),
        (15, False, True, "open"),
        (0, False, True, "late"),
    ],
)
def test_arrival_status_branches(
    minutes_early, is_colour, is_weekend, expected
):
    assert arrival_status(minutes_early, is_colour, is_weekend) == expected
