needed_sum = int(input())
n = 0
y = 0
z = 0
cash = 0
card = 0

while True:
    if cash + card >= needed_sum:
        print(f"Average CS: {cash / z:.2f}")
        print(f"Average CC: {card / y:.2f}")
        break

    if needed_sum >= cash + card:
        n += 1

    price_stocks = input()
    if price_stocks == "End":
        print("Failed to collect required money for charity.")
        break

    if n % 2 == 0:
        if int(price_stocks) >= 10:
            y += 1
            card += int(price_stocks)
            print("Product sold!")
        elif int(price_stocks) < 10:
            print("Error in transaction!")
            continue

    else:
        if int(price_stocks) <= 100:
            z += 1
            cash += int(price_stocks)
            print("Product sold!")
        elif int(price_stocks) > 100:
            print("Error in transaction!")
            continue