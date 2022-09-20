from math import ceil
height = int(input())
width = int(input())
not_painted_perc = int(input())
area = height * width * 4
total_area = ceil(area * (1 - not_painted_perc / 100))
command = ""
while True:
    command = input()
    if command == "Tired!":
        print(f"{int(ceil(total_area))} quadratic m left.")
        break
    l_paint = int(command)
    total_area -= l_paint

    if total_area < 0:
        print(f"All walls are painted and you have {abs(int(total_area))} l paint left!")
        break
    elif total_area == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break