budget = float(input())
season = input()

cost = 0
destination = ""
place = ""

if budget > 1000:
    destination = "Europe"
    cost = budget * 0.9
    place = "Hotel"

elif budget > 100:
    destination = "Balkans"
    if season == "summer":
        cost = budget * 0.4
        place = "Camp"
    elif season == "winter":
        cost = budget * 0.8
        place = "Hotel"

else:
    destination = "Bulgaria"
    if season == "summer":
        cost = budget * 0.3
        place = "Camp"
    elif season == "winter":
        cost = budget * 0.7
        place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {cost:.2f}")