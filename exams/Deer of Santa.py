from math import ceil

days_without_santa = int(input())
left_food_per_kg = int(input())
food_for_1st_deer_for_day = float(input())
food_for_2nd_deer_for_day = float(input())
food_for_3rd_deer_for_day = float(input())

food_deer = (food_for_1st_deer_for_day + food_for_2nd_deer_for_day + food_for_3rd_deer_for_day) * days_without_santa
diff = left_food_per_kg - food_deer

if diff >= 0:
    print(f"{int(diff)} kilos of food left.")
else:
    print(f"{ceil(abs(diff))} more kilos of food are needed.")
