while True:
    destination = input()

    if destination == "End":
        break
    needed_budget = float(input())
    money = 0
    while money < needed_budget:
        collect_sum = float(input())

        if collect_sum == "End":
            break
        money += float(collect_sum)

        if money >= needed_budget:
            print(f"Going to {destination}!")
            break