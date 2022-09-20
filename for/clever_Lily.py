lilis_years = int(input())
washer_price = float(input())
price_for_toy = int(input())

toys = 0
money = 0
sold_toys = 0
brother_tax = 0

for i in range(1, lilis_years + 1):
    if i % 2 != 0:
        toys += 1
        sold_toys += 1
    else:
        money += 5 * i
        brother_tax += 1

profit_toys = sold_toys * price_for_toy

total_sum = profit_toys + money - brother_tax
left_price = total_sum - washer_price

if left_price >= 0:
    print(f"Yes! {left_price:.2f}")
else:
    print(f"No! {abs(left_price):.2f}")
