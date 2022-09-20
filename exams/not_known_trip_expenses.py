days = int(input())
day_cost = 0
rest = 0
count = 0
for day in range(days):
    command = input()
    day_cost = 60 + rest
    count = 0
    while True:
        if command == "Day over":
            rest = day_cost
            print(f"Money left from today: {day_cost:.2f}. You've bought {count} products.")
            #day_cost = 0
            break
        price = float(command)
        day_cost -= price
        count += 1

        if day_cost == 0:
            print(f"Daily limit exceeded! You've bought {count} products.")
            enough_money = False
            break
        elif day_cost < 0:
            day_cost += price
            count -= 1
            command = input()
            continue

        command = input()