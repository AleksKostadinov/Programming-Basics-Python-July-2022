budget = float(input())
product = input()
count = 0
total = 0
diff = 0
is_enough = True
while product != "Stop":
    price = float(input())

    count += 1
    if count % 3 == 0:
        price *= 0.5
    diff = price - budget
    if price > budget:
        is_enough = False
        print(f"You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break
    total += price
    budget -= price

    product = input()

if is_enough:
    print(f"You bought {count} products for {total:.2f} leva.")