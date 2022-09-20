command = input()
climbed_meters = int(input())
days = 1
started_meters = 5364
total_climbed_meters = 0
goal_reached = False
while command != "END":

    if command == "Yes":
        days += 1
    total_climbed_meters += climbed_meters + started_meters
    started_meters = 0

    if total_climbed_meters >= 8848:
        goal_reached = True
        break

    if days == 5:
        break

    command = input()
    if command == "END":
        break

    climbed_meters = int(input())

if goal_reached:
    print(f"Goal reached for {days} days!")
else:
    print(f"Failed!\n{total_climbed_meters}")