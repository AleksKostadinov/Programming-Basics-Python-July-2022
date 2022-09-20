budget = float(input())
number_serials = int(input())

for _ in range(number_serials):
    serial = input()
    price = float(input())

    if serial == "Thrones":
        price *= 0.5
    elif serial == "Lucifer":
        price *= 0.6
    elif serial == "Protector":
        price *= 0.7
    elif serial == "TotalDrama":
        price *= 0.8
    elif serial == "Area":
        price *= 0.9
    else:
        price *= 1
    budget -= price

if budget < 0:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")
else:
    print(f"You bought all the series and left with {budget:.2f} lv.")