budget = float(input())
season = input()

if budget <= 100:
    if season == "summer":
        cost = budget * 0.3
        print(f"Somewhere in Bulgaria")
        print(f"Camp - {cost:.2f}")
    else:
        cost = budget * 0.7
        print(f"Somewhere in Bulgaria")
        print(f"Hotel - {cost:.2f}")
elif 100 < budget <= 1000:
    if season == "summer":
        cost = budget * 0.4
        print(f"Somewhere in Balkans")
        print(f"Camp - {cost:.2f}")
    else:
        cost = budget * 0.8
        print(f"Somewhere in Balkans")
        print(f"Hotel - {cost:.2f}")
else:
    cost = budget * 0.9
    print(f"Somewhere in Europe")
    print(f"Hotel - {cost:.2f}")