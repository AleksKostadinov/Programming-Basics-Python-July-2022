width = int(input())
length = int(input())
height = int(input())
command = input()
volume = width * length * height
boxes = 0
no_space = False
while command != "Done":
    number_boxes = int(command)
    volume -= number_boxes
    if volume < 0:
        no_space = True
        break
    command = input()
if no_space:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")
else:
    print(f"{volume} Cubic meters left.")