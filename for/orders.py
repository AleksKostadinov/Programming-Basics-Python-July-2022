num_orders = int(input())
total_sum = 0

for i in range(1, num_orders + 1):
    price_per_caps = float(input())
    days = int(input())
    caps_per_day = int(input())

    if 1 <= caps_per_day <= 2000 and 0.01 <= price_per_caps <= 100 and 1 <= days <= 31:
        total_per_order = price_per_caps * (days * caps_per_day)
        total_sum += total_per_order
        print(f"The price for the coffee is: ${total_per_order:.2f}")
    else:
        continue

print(f'Total: ${total_sum:.2f}')
