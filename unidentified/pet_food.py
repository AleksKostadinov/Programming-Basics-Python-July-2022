from math import floor
from math import ceil
days = int(input())
opening_food = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

final_dog_food = dog_food_kg * days
final_cat_food = cat_food_kg * days
final_turtle_food = turtle_food_gr * days / 1000
total_food = final_dog_food + final_cat_food + final_turtle_food
rest_food = opening_food - total_food

if total_food <= opening_food:
    print(f"{floor(rest_food)} kilos of food left.")
else:
    print(f"{ceil(abs(rest_food))} more kilos of food are needed.")

