from math import ceil

guests = int(input())
budget = int(input())
bread = ceil(guests / 3)
eggs = guests * 2

cost = bread * 4 + eggs * 0.45
diff = budget - cost

if budget >= cost:
    print(f"Lyubo bought {bread} Easter bread and {eggs} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {abs(diff):.2f} lv. more.")

