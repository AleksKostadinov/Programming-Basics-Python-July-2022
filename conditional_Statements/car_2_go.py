budget = float(input())
season = input()
class_car = ""
car_type = ""

if budget <= 100:
  class_car = "Economy class"
  if season == "Summer":
    car = 0.35
    car_type = "Cabrio"
  elif season == "Winter":
    car = 0.65
    car_type = "Jeep"
elif 100 < budget <= 500:
  class_car = "Compact class"
  if season == "Summer":
    car = 0.45
    car_type = "Cabrio"
  elif season == "Winter":
    car = 0.80
    car_type = "Jeep"
elif budget > 500:
    class_car = "Luxury class"
    car = 0.9
    car_type = "Jeep"

price = budget * car

print(class_car)
print(f"{car_type} - {price:.2f}")