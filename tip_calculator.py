def calculate_tip(bill, tip_percent):
    tip = bill * tip_percent / 100
    total = bill + tip

    return {
        "tip": tip,
        "total": total
    }

bills = [500, 1200, 2500]

for bill in bills:
    result = calculate_tip(bill, 10)

    print(f"Bill Amount: {bill}")
    print(f"Tip Amount: {result['tip']}")
    print(f"Total Amount: {result['total']}\n")