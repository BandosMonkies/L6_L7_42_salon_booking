import pytest

from salon_booking import arrival_status, can_book, extra_time_charge


def test_extra_time_charge_rejects_unknown_service():
    with pytest.raises(ValueError, match="unknown service"):
        extra_time_charge("nails", 30, "junior", False)


def test_extra_time_charge_rejects_negative_duration():
    with pytest.raises(ValueError, match="invalid duration"):
        extra_time_charge("haircut", -1, "junior", False)


def test_extra_time_charge_within_included_time():
    assert extra_time_charge("haircut", 20, "junior", False) == 0


def test_extra_time_charge_uses_junior_rate():
    assert extra_time_charge("haircut", 40, "junior", False) == 100


def test_extra_time_charge_uses_non_junior_rate():
    assert extra_time_charge("spa", 100, "senior", False) == 180


def test_member_gets_extra_time_for_non_spa_service():
    assert extra_time_charge("colour", 80, "junior", True) == 50


def test_extra_time_charge_adds_long_booking_senior_surcharge():
    assert extra_time_charge("haircut", 100, "senior", False) == 2100


def test_can_book_walk_in_and_regular_booking():
    assert can_book(2, 1, True) is True
    assert can_book(3, 1, True) is False
    assert can_book(4, 2, False) is True
    assert can_book(4, 3, False) is False
    assert can_book(5, 1, False) is False


def test_arrival_status_reports_each_status():
    assert arrival_status(10, False, False) == "open"
    assert arrival_status(0, False, False) == "late"
    assert arrival_status(-16, False, False) == "closed"
