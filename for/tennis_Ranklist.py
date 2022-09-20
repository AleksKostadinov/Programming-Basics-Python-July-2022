from math import floor
number_tournaments = int(input())
start_points = int(input())

add_points = 0
wins = 0
for i in range(1, number_tournaments + 1):
    stage = input()

    if stage == "W":
        wins += 1
        add_points += 2000
    elif stage == "F":
        add_points += 1200
    else:
        add_points += 720

total_points = start_points + add_points
average_points = floor(add_points / number_tournaments)
win_tournaments = (wins / number_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{win_tournaments:.2f}%")