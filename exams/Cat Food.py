number_cats = int(input())
small_cat = 0
big_cat = 0
huge_cat = 0
total_food_gr = 0
for cat in range(1, number_cats + 1):
    eaten_food_gr = float(input())

    if 100 <= eaten_food_gr < 200:
        small_cat += 1
    elif 200 <= eaten_food_gr < 300:
        big_cat += 1
    elif 300 <= eaten_food_gr < 400:
        huge_cat += 1
    total_food_gr += eaten_food_gr

eaten_food_kg = total_food_gr / 1000

total_price = eaten_food_kg * 12.45

print(f"Group 1: {small_cat} cats.")
print(f"Group 2: {big_cat} cats.")
print(f"Group 3: {huge_cat} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")