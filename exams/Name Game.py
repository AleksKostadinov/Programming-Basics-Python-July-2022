player = input()
points = 0
max_points = 0
winner = ""
while True:
    length = len(player)
    for i in range(0, length):
        n = int(input())
        if n == ord(player[i]):
            points += 10
        else:
            points += 2
    if points >= max_points:
        max_points = points
        winner = player
    player = input()
    points = 0
    if player == "Stop":
        break

print(f"The winner is {winner} with {max_points} points!")