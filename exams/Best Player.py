player = input()

command = ""
max_goals = -1
best_player = ""
made_hat_trick = False
while player != "END":
    goals = int(input())

    if goals > max_goals:
        max_goals = goals
        best_player = player
        if max_goals >= 3:
            made_hat_trick = True
    if goals >= 10:
        break
    player = input()

print(f"{best_player} is the best player!")

if made_hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")