num_bread = int(input())
max_chef_pt = 0
max_chef_name = ""

for chefs in range(num_bread):
    chef = input()
    points = 0
    command = input()
    while command != "Stop":
        rating = int(command)
        points += rating
        command = input()

    print(f"{chef} has {points} points.")
    if points > max_chef_pt:
        max_chef_pt = points
        max_chef_name = chef
        print(f"{max_chef_name} is the new number 1!")

print(f"{max_chef_name} won competition with {max_chef_pt} points!")
