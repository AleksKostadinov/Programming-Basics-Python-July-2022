season = input()
km_per_month = float(input())
tax = 0.10

if 10000 < km_per_month <= 20000:
  price = 1.45
elif 5000 < km_per_month <= 10000:
  if season == "Spring" or season == "Autumn":
    price = 0.95
  elif season == "Summer":
    price = 1.10
  else:
    price = 1.25
else:
  if season == "Spring" or season == "Autumn":
    price = 0.75
  elif season == "Summer":
    price = 0.90
  else:
    price = 1.05

total_price_per_month = price * km_per_month
total_price = total_price_per_month * 4 * (1 - tax)

print(f"{total_price:.2f}")