quantity = int(input())
days = int(input())
total_quantity = 0
points = 0
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 10 == 0:
        points -= 20
        total_quantity += (tree_skirt + tree_garlands + tree_lights) * 1
        if i == days:
            points -= 30
    if i % 5 == 0:
        total_quantity += quantity * tree_lights
        points += 17
        if i % 3 == 0:
            points += 30
    if i % 3 == 0:
        total_quantity += quantity * (tree_skirt + tree_garlands)
        points += 13
    if i % 2 == 0:
        total_quantity += quantity * ornament_set
        points += 5

print(f"Total cost: {total_quantity}")
print(f"Total spirit: {points}")
