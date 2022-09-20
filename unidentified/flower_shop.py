from math import floor
from math import ceil

magnolia = int(input()) # 3.25
zumbul = int(input())   # 4.00
rose = int(input())     # 3.50
cactus = int(input())   # 8.00
gift_price = float(input())

tax = 0.05

profit_magnolia = magnolia * 3.25
profit_rose = rose * 3.50
profit_zumbul = zumbul * 4
profit_cactus = cactus * 8
total_profit = (profit_magnolia + profit_rose + profit_zumbul + profit_cactus) * (1 - 0.05)
profit_difference = total_profit - gift_price

if total_profit >= gift_price:
    print(f"She is left with {int(floor(profit_difference))} leva.")
else:
    print(f"She will have to borrow {int(ceil(abs(profit_difference)))} leva.")

