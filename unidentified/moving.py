width = int(input())
length = int(input())
height = int(input())
volume = width * length * height
command = input()
total_num = 0
while command != "Done":
    num = int(command)
    total_num += num

    if volume < total_num:
        break
    command = input()

available = volume - total_num
if volume > total_num:
    print(f"{available} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(available)} Cubic meters more.")