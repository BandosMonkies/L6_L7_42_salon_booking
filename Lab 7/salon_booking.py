import math


def parse_booking(text):
    if not isinstance(text, str) or text.count(":") != 1:
        raise ValueError("booking must use the format service:minutes")
    service, minutes_text = (part.strip() for part in text.split(":"))
    try:
        minutes = float(minutes_text)
    except ValueError as error:
        raise ValueError("minutes must be a number") from error
    if not service or not math.isfinite(minutes) or minutes < 0:
        raise ValueError("service must be non-empty and minutes cannot be negative")
    return service.title(), minutes

def duration_average(durations_csv):
    if not isinstance(durations_csv, str) or not durations_csv.strip():
        raise ValueError("durations must be a non-empty comma-separated list")
    try:
        values = [int(item.strip()) for item in durations_csv.split(",")]
    except ValueError as error:
        raise ValueError("durations must contain only integers") from error
    if not values:
        raise ValueError("durations must contain at least one value")
    return sum(values) // len(values)

def payable_bill(text):
    if not isinstance(text, str) or text.count("|") != 1:
        raise ValueError("bill must use the format bill|discount")
    bill_text, discount_text = (part.strip() for part in text.split("|"))
    try:
        bill = float(bill_text)
        discount = float(discount_text)
    except ValueError as error:
        raise ValueError("bill and discount must be numbers") from error
    if (
        not math.isfinite(bill)
        or not math.isfinite(discount)
        or bill < 0
        or discount < 0
    ):
        raise ValueError("bill and discount cannot be negative")
    total = bill * 1.18 - discount
    return max(total, 0)

def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter service:duration in min (e.g. haircut:45): ")
    try:
        result = parse_booking(user_input)
        print("Service and Duration:", result)
    except ValueError as error:
        print("Invalid booking:", error)

    print("\n==== Running duration_average ====")
    user_input = input("Enter durations as CSV (e.g. 30,45,60): ")
    try:
        result = duration_average(user_input)
        print("Average Duration:", result)
    except ValueError as error:
        print("Invalid durations:", error)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 800|100): ")
    try:
        result = payable_bill(user_input)
        print("Payable Bill:", result)
    except ValueError as error:
        print("Invalid bill:", error)

if __name__ == "__main__":
    main()
