budget = float(input())
category = input()
number = int(input())

total_budget = 0
pure_budget = 0
ticket = 0

if category == "VIP":
    ticket = 499.99
elif category == "Normal":
    ticket = 249.99

if 1 <= number <= 4:
    pure_budget = budget * (1 - 0.75)

elif 5 <= number <= 9:
    pure_budget = budget * (1 - 0.60)

elif 10 <= number <= 24:
    pure_budget = budget * (1 - 0.50)

elif 25 <= number <= 49:
    pure_budget = budget * (1 - 0.40)

elif number >= 50:
    pure_budget = budget * (1 - 0.25)

sum_ticket = ticket * number
total_budget = pure_budget - sum_ticket

if total_budget >= 0:
    print(f"Yes! You have {total_budget:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(total_budget):.2f} leva.")