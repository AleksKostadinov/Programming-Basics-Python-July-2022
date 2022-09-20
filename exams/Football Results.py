win = 0
lost = 0
draw = 0

for _ in range(3):
    game = input()
    if game[0] > game[2]:
        win += 1
    elif game[0] < game[2]:
        lost += 1
    elif game[0] == game[2]:
        draw += 1

print(f"Team won {win} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draw}")