# L6_L7_42 — Salon Booking

Lab 7: Fuzz Testing

## About

A small Python module that parses salon bookings, averages service durations and works out the payable bill after a discount.

## Files

| File | Description |
|------|-------------|
| `salon_booking.py` | The code under test |
| `test_salon_booking.py` | Starter test file |

Refer to the lab handout for instructions.

## Run the fuzz tests

From the repository root, run:

```bash
.venv/bin/python -m pytest -q "Lab 7/test_salon_booking.py"
```

The tests use Hypothesis to generate text and `None` values for all three
functions. Invalid inputs raise clear `ValueError` exceptions, while the
interactive application reports the validation error and continues running.
Valid inputs retain the original behavior.
