season = input()
types = input()
number = int(input())
nights = int(input())

discount = 0
sport = ""

if number >= 50:
  discount = 0.50
elif 20 <= number < 50:
  discount = 0.15
elif 10 <= number < 20:
  discount = 0.05

if types == "boys" or types == "girls":
  if season == "Winter":
    price_per_night = 9.60
  elif season == "Spring":
    price_per_night = 7.20
  elif season == "Summer":
    price_per_night = 15.00
else:
  if season == "Winter":
    price_per_night = 10
  elif season == "Spring":
    price_per_night = 9.5
  elif season == "Summer":
    price_per_night = 20.00

if season == "Winter":
  if types == "girls":
    sport = "Gymnastics"
  elif types == "boys":
    sport = "Judo"
  elif types == "mixed":
    sport = "Ski"
elif season == "Spring":
  if types == "girls":
    sport = "Athletics"
  elif types == "boys":
    sport = "Tennis"
  elif types == "mixed":
    sport = "Cycling"
elif season == "Summer":
  if types == "girls":
    sport = "Volleyball"
  elif types == "boys":
    sport = "Football"
  elif types == "mixed":
    sport = "Swimming"

price = number * nights * price_per_night * (1 - discount)
print(f"{sport} {price:.2f} lv.")