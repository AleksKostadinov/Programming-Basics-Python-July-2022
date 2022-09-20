player = input()
command = input()
start_points = 301
is_retired = True
bad_strikes = 0
count = 0
while command != "Retire":

    points = int(input())
    count += 1
    if command == "Single":
        start_points -= points
        if 0 > start_points:
            start_points += points
            bad_strikes += 1
    elif command == "Double":
        start_points -= points * 2
        if 0 > start_points:
            start_points += points * 2
            bad_strikes += 1
    elif command == "Triple":
        start_points -= points * 3
        if 0 > start_points:
            start_points += points * 3
            bad_strikes += 1

    if start_points <= 0:
        is_retired = False
        break

    command = input()

if is_retired:
    print(f"{player} retired after {bad_strikes} unsuccessful shots.")
else:
    diff = count-bad_strikes
    print(f"{player} won the leg with {diff} shots.")
