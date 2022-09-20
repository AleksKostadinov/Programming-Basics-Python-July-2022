days = int(input())
room = input()
rate = input()
nights_rest = days - 1

if days <= 10:
    if room == "apartment":
        price = 0.7 * 25
    elif room == "president apartment":
        price = 0.9 * 35
    else:
        price = 18
elif days <= 16:
    if room == "apartment":
        price = 0.65 * 25
    elif room == "president apartment":
        price = 0.85 * 35
    else:
        price = 18
else:
    if room == "apartment":
        price = 0.5 * 25
    elif room == "president apartment":
        price = 0.8 * 35
    else:
        price = 18

if rate == "positive":
    total = price * 1.25 * nights_rest
else:
    total = price * 0.9 * nights_rest

print(f"{total:.2f}")
