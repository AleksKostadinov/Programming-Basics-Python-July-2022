cake_width = int(input())
cake_length = int(input())
area = cake_length * cake_width

pieces_count = 0

while area > pieces_count:
    command = input()

    if command == "STOP":
        break

    pieces_count += int(command)

pieces_display = abs(area - pieces_count)

if area > pieces_count:
    print(f"{pieces_display} pieces are left.")
else:
    print(f"No more cake left! You need {pieces_display} pieces more.")