purpose_for_day = int(input())
command = input()
price = 0
got_purposed = False
while command != "closed":
    if command == "haircut":
        command = input()
        if command == "closed":
            break
        if command == "mens":
            price += 15
        elif command == "ladies":
            price += 20
        elif command == "kids":
            price += 10

    elif command == "color":
        command = input()
        if command == "closed":
            break
        if command == "touch up":
            price += 20
        elif command == "full color":
            price += 30

    if purpose_for_day <= price:
        got_purposed = True
        break
    command = input()

if not got_purposed:
    diff = purpose_for_day - price
    print(f"Target not reached! You need {diff}lv. more.")
elif got_purposed:
    print("You have reached your target for the day!")
print(f"Earned money: {price}lv.")

