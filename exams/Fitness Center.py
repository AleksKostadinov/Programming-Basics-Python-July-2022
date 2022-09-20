people = int(input())
training_back = 0
training_chest = 0
training_legs = 0
training_abs = 0
bought_shake = 0
bought_bar = 0
for i in range(people):
    activity = input()
    if activity == "Back":
        training_back += 1
    elif activity == "Chest":
        training_chest += 1
    elif activity == "Legs":
        training_legs += 1
    elif activity == "Abs":
        training_abs += 1
    elif activity == "Protein shake":
        bought_shake += 1
    elif activity == "Protein bar":
        bought_bar += 1

perc_protein = ((bought_shake + bought_bar) / people) * 100
perc_workout = 100 - perc_protein

print(f"{training_back} - back")
print(f"{training_chest} - chest")
print(f"{training_legs} - legs")
print(f"{training_abs} - abs")
print(f"{bought_shake} - protein shake")
print(f"{bought_bar} - protein bar")
print(f"{perc_workout:.2f}% - work out")
print(f"{perc_protein:.2f}% - protein")
