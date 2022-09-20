budget = float(input())
people = int(input())
dress_per_person = float(input())

decor = budget * 0.1

if people > 150:
    dress_per_person = dress_per_person * 0.9

price = people * dress_per_person + decor
diff = price - budget
if price > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {abs(diff):.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {abs(diff):.2f} leva left.")
