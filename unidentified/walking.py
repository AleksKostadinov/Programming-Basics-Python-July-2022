walking = input()
summ = 0

while walking != "Going home":
    steps = int(walking)
    summ += steps
    if summ >= 10000:
        print(f"Goal reached! Good job!")
        print(f"{summ - 10000} steps over the goal!")
        break
    else:
        walking = input()

if walking == "Going home":
    steps = int(input())
    summ += steps
    if summ < 10000:
        print(f"{10000 - summ} more steps to reach goal.")
    else:
        print(f"Goal reached! Good job!")
        print(f"{summ - 10000} steps over the goal!")