days = int(input())
total_food = float(input())
biscuits = 0
total_eaten_food = 0
days_eaten_by_dog = 0
days_eaten_by_cat = 0
for day in range(1, days + 1):
    eaten_by_dog = int(input())
    eaten_by_cat = int(input())

    day_eaten = eaten_by_dog + eaten_by_cat
    days_eaten_by_dog += eaten_by_dog
    days_eaten_by_cat += eaten_by_cat
    total_eaten_food += eaten_by_dog + eaten_by_cat

    if day % 3 == 0:
        biscuits += day_eaten * 0.1

print(f"Total eaten biscuits: {round(biscuits)}gr.")

perc_eaten_food = (total_eaten_food / total_food) * 100
print(f"{perc_eaten_food:.2f}% of the food has been eaten.")

perc_eaten_food_by_dog = (days_eaten_by_dog / total_eaten_food) * 100
print(f"{perc_eaten_food_by_dog:.2f}% eaten from the dog.")

perc_eaten_food_by_cat = (days_eaten_by_cat / total_eaten_food) * 100
print(f"{perc_eaten_food_by_cat:.2f}% eaten from the cat.")