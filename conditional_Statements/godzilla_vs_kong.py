budget = float(input())
people = int(input())
dress = float(input())
dress_discount = 0
decor = budget * 10 / 100
dress_people = 0
total = 0
if people <= 150:
    dress_people = dress * people
    total = budget - (dress_people + decor)

if people > 150:
    dress_discount = dress * 10 / 100
    dress_people = (dress - dress_discount) * people
    total = budget - (dress_people + decor)

if budget >= decor + dress_people:
    print("Action!")
    print(f"Wingard starts filming with {total:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(total):.2f} leva more.")
