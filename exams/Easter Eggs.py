number_of_coloured_eggs = int(input())
red_count = 0
orange_count = 0
blue_count = 0
green_count = 0
max_colour = ""
max_count = -1
for egg in range(1, number_of_coloured_eggs + 1):
    colour = input()
    if colour == "red":
        red_count += 1
    elif colour == "orange":
        orange_count += 1
    elif colour == "blue":
        blue_count += 1
    else:
        green_count += 1

if green_count >= max_count:
    max_count = green_count
    max_colour = "green"
if red_count >= max_count:
    max_count = red_count
    max_colour = "red"
if orange_count >= max_count:
    max_count = orange_count
    max_colour = "orange"
if blue_count >= max_count:
    max_count = blue_count
    max_colour = "blue"

print(f"Red eggs: {red_count}")
print(f"Orange eggs: {orange_count}")
print(f"Blue eggs: {blue_count}")
print(f"Green eggs: {green_count}")
print(f"Max eggs: {max_count} -> {max_colour}")
