budget = float(input())
product = input()
count = 0
total = 0
diff = 0
while product != "Stop":
    price = float(input())
    count += 1
    if count % 3 == 0:
        price *= 0.5

    if price > budget:
        diff = price - budget
        print(f"You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break
    total += price
    budget -= price

    product = input()

if product == "Stop":
    print(f"You bought {count} products for {total:.2f} leva.")

