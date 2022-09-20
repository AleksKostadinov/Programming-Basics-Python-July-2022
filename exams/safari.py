budget = float(input())
liters = float(input())
day = input()

if day == "Saturday":
    discount = 0.9
else:
    discount = 0.8

diff = budget - ((liters * 2.1 + 100) * discount)

if diff >= 0:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {abs(diff):.2f} lv.")