number = input()
balance = 0

while number != "NoMoreMoney":
    amount = float(number)
    if amount < 0:
        print("Invalid operation!")
        break

    else:
        print(f"Increase: {amount:.2f}")
        balance += amount
        number = input()
print(f"Total: {balance:.2f}")