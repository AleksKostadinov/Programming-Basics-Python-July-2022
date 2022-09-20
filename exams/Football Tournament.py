team = input()
matches = int(input())
points = 0
count_w = 0
count_d = 0
count_l = 0

for i in range(1, matches + 1):
    result = input()
    if result == "W":
        points += 3
        count_w += 1
    if result == "D":
        points += 1
        count_d += 1
    if result == "L":
        points += 0
        count_l += 1

if matches == 0:
    print(f"{team} hasn't played any games during this season.")

else:
    win_rate = (count_w / matches) * 100
    print(f"{team} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {count_w}")
    print(f"## D: {count_d}")
    print(f"## L: {count_l}")
    print(f"Win rate: {win_rate:.2f}%")
