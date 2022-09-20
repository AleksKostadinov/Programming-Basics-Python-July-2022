guests = int(input())
price_per_guest = float(input())
budget = float(input())
cake = budget * 0.10
if guests < 10:
    price_per_guest *= 1
elif guests <= 15:
    price_per_guest *= 0.85
elif guests <= 20:
    price_per_guest *= 0.8
else:
    price_per_guest *= 0.75

cost = guests * price_per_guest + cake
diff = budget - cost
if budget >= cost:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {abs(diff):.2f} leva needed.")