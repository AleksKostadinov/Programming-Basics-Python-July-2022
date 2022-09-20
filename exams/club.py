expected_budget = float(input())
command = input()
profit = 0
diff = 0

while command != "Party!":
    number = int(input())
    price_cocktail = len(command)
    current_order = price_cocktail * number

    if current_order % 2 != 0:
        price_cocktail *= 0.75
    profit += price_cocktail * number
    diff = expected_budget - profit

    if profit >= expected_budget:
        print(f"Target acquired.")
        break

    command = input()
if command == "Party!":
    print(f"We need {abs(diff):.2f} leva more.")

print(f"Club income - {profit:.2f} leva.")