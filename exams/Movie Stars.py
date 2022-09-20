budget = float(input())
command = input()
enough_budget = True
while command != "ACTION":
    length = len(command)
    if length <= 15:
        wage = float(input())
    else:
        wage = budget * 0.2

    budget -= wage

    if budget < 0:
        enough_budget = False
        break
    command = input()

if enough_budget:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")