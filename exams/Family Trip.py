budget = float(input())
nights = int(input())
price_night = float(input())
extra_cost = int(input())

if nights > 7:
    price_night *= 0.95
costs = nights * price_night + budget * (extra_cost / 100)
diff = budget - costs
if diff >= 0:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{abs(diff):.2f} leva needed.")
