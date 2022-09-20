clients = int(input())
total = 0
for i in range(1, clients + 1):
    price = 0
    count = 0
    command = input()
    while command != "Finish":
        if command == "basket":
            price += 1.50
        elif command == "wreath":
            price += 3.8
        elif command == "chocolate bunny":
            price += 7
        count += 1
        command = input()

    if count % 2 == 0:
        price *= 0.8
    print(f"You purchased {count} items for {price:.2f} leva.")
    total += price
avg = total / clients
print(f"Average bill per client is: {avg:.2f} leva.")