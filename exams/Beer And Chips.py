from math import ceil
fan_name = input()
budget = float(input())
bottles_beer = int(input())
packets_chips = int(input())

price_beers = bottles_beer * 1.2
price_for_one_chips = price_beers * 0.45
price_chips = price_for_one_chips * packets_chips
total_price = price_beers + ceil(price_chips)
diff = budget - total_price
if total_price <= budget:
    print(f"{fan_name} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{fan_name} needs {abs(diff):.2f} more leva!")
