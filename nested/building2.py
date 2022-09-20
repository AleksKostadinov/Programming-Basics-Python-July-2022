floors = int(input())  # 6
rooms = int(input())  # 4

for current_floor in range(floors, 0, -1):
    for room in range(rooms):
        if current_floor == floors:
            floor_letter = "L"
        elif current_floor % 2 == 0:
            floor_letter = "O"
        else:
            floor_letter = "A"
        print(f'{floor_letter}{current_floor}{room}', end=' ')
    print()