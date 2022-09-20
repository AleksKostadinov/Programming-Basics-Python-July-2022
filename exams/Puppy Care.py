bought_food_kg = int(input())
eaten_food_gr = int(input())
bought_food_gr = bought_food_kg * 1000
command = str(eaten_food_gr)
eaten = 0

while command != "Adopted":
    eaten_food_gr = int(command)
    eaten += eaten_food_gr

    command = input()
diff = bought_food_gr - eaten
if bought_food_gr >= eaten:
    print(f"Food is enough! Leftovers: {diff} grams." )
else:
    print(f"Food is not enough. You need {abs(diff)} grams more." )