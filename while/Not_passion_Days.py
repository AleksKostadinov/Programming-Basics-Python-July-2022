budget = float(input())
command = input()
purchase = 0

while command != "mall.Enter":
    command = input()
command = input()
while command != "mall.Exit":
    for action in command:
        if action.isupper():
            price = 0.50 * ord(action)
            if price > budget:
                continue
            else:
                budget -= price
                purchase += 1
        elif action.islower():
            price = 0.3 * ord(action)
            if price > budget:
                continue
            else:
                budget -= price
                purchase += 1
        elif action == "%":
            if budget != 0:
                price = budget / 2
                if price > budget:
                    continue
                else:
                    budget = price
                    purchase += 1
        elif action == "*":
            budget += 10
            continue
        else:
            price = ord(action)
            if price > budget:
                continue
            else:
                budget -= price
                purchase += 1

    command = input()
    if command == "mall.Exit":
        break
if purchase > 0:
    print(f"{purchase} purchases. Money left: {budget:.2f} lv.")
else:
    print(f"No purchases. Money left: {budget:.2f} lv.")