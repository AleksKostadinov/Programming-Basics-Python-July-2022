weight_kg = float(input())
service = input()
distance = int(input())
total_price = 0
markup = 0
up = 0
if weight_kg < 1:
    price = 3 / 100
    if service == "express":
        up = 0.8
elif weight_kg < 10:
    price = 5 / 100
    if service == "express":
        up = 0.4
elif weight_kg < 40:
    price = 10 / 100
    if service == "express":
        up = 0.05
elif weight_kg < 90:
    price = 15 / 100
    if service == "express":
        up = 0.02
else:
    price = 20 / 100
    if service == "express":
        up = 0.01
markup = price * up * weight_kg * distance
total_price = price * distance + markup

print(f"The delivery of your shipment with weight of {weight_kg:.3f} kg. would cost {total_price:.2f} lv.")
