bought_food_kg = int(input())
command = input()
not_enough = False
bought_food_gr = bought_food_kg * 1000
while command != "Adopted":
    current_eaten = int(command)

    bought_food_gr -= current_eaten
    if bought_food_gr < 0:
        not_enough = True

    command = input()

if not_enough:
    print(f"Food is not enough. You need {abs(bought_food_gr)} grams more.")
else:
    print(f"Food is enough! Leftovers: {bought_food_gr} grams.")