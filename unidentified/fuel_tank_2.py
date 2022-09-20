fuel = input()
liters = float(input())
card = input()

if liters > 25:
  discount_lt = 0.1
  if fuel == "Gasoline":
    price_fuel = 2.22
    if card == "Yes":
      dicount_card = 0.18
    else:
      dicount_card = 0
  elif fuel == "Diesel":
    price_fuel = 2.33
    if card == "Yes":
      dicount_card = 0.12
    else:
      dicount_card = 0
  elif fuel == "Gas":
    price_fuel = 0.93
    if card == "Yes":
      dicount_card = 0.08
    else:
      dicount_card = 0

elif 20 <= liters <= 25:
  discount_lt = 0.08
  if fuel == "Gasoline":
    price_fuel = 2.22
    if card == "Yes":
      dicount_card = 0.18
    else:
      dicount_card = 0
  elif fuel == "Diesel":
    price_fuel = 2.33
    if card == "Yes":
      dicount_card = 0.12
    else:
      dicount_card = 0
  elif fuel == "Gas":
    price_fuel = 0.93
    if card == "Yes":
      dicount_card = 0.08
    else:
      dicount_card = 0

else:
  discount_lt = 0
  if fuel == "Gasoline":
      price_fuel = 2.22
      if card == "Yes":
        dicount_card = 0.18
      else:
        dicount_card = 0
  elif fuel == "Diesel":
      price_fuel = 2.33
      if card == "Yes":
        dicount_card = 0.12
      else:
        dicount_card = 0
  elif fuel == "Gas":
      price_fuel = 0.93
      if card == "Yes":
        dicount_card = 0.08
      else:
        dicount_card = 0

price = liters * (price_fuel - dicount_card) * (1 - discount_lt)
print(f"{price:.2f} lv.")