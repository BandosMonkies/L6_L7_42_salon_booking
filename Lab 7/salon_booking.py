import math


def parse_booking(text):
    if not isinstance(text, str) or text.count(":") != 1:
        return "", 0.0
    service, minutes_text = (part.strip() for part in text.split(":"))
    try:
        minutes = float(minutes_text)
    except ValueError:
        return "", 0.0
    if not service or not math.isfinite(minutes) or minutes < 0:
        return "", 0.0
    return service.title(), minutes

def duration_average(durations_csv):
    if not isinstance(durations_csv, str) or not durations_csv.strip():
        return 0
    try:
        values = [int(item.strip()) for item in durations_csv.split(",")]
    except ValueError:
        return 0
    return sum(values) // len(values) if values else 0

def payable_bill(text):
    if not isinstance(text, str) or text.count("|") != 1:
        return 0.0
    bill_text, discount_text = (part.strip() for part in text.split("|"))
    try:
        bill = float(bill_text)
        discount = float(discount_text)
    except ValueError:
        return 0.0
    if (
        not math.isfinite(bill)
        or not math.isfinite(discount)
        or bill < 0
        or discount < 0
    ):
        return 0.0
    total = bill * 1.18 - discount
    return max(total, 0)

def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter service:duration in min (e.g. haircut:45): ")
    result = parse_booking(user_input)
    print("Service and Duration:", result)

    print("\n==== Running duration_average ====")
    user_input = input("Enter durations as CSV (e.g. 30,45,60): ")
    result = duration_average(user_input)
    print("Average Duration:", result)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 800|100): ")
    result = payable_bill(user_input)
    print("Payable Bill:", result)

if __name__ == "__main__":
    main()
