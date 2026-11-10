from hypothesis import given, strategies as st
from salon_booking import parse_booking, duration_average, payable_bill


@given(st.text() | st.none())
def test_parse_booking_no_crash(s):
    result = parse_booking(s)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], float)


@given(st.text() | st.none())
def test_duration_average_no_crash(s):
    result = duration_average(s)
    assert isinstance(result, int)


@given(st.text() | st.none())
def test_payable_bill_no_crash(s):
    result = payable_bill(s)
    assert isinstance(result, float)


def test_valid_booking_is_parsed():
    assert parse_booking(" haircut:45 ") == ("Haircut", 45.0)


def test_valid_durations_are_averaged():
    assert duration_average("30, 45, 60") == 45


def test_valid_bill_applies_tax_and_discount():
    assert payable_bill("800|100") == 844.0


def test_invalid_inputs_use_safe_defaults():
    assert parse_booking("haircut") == ("", 0.0)
    assert duration_average("") == 0
    assert payable_bill("800") == 0.0
