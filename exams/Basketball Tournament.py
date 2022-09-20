tournament = input()
count = 0
win_games = 0
command = ""
while command != "End of tournaments":
    n_games = int(input())

    for i in range(1, n_games + 1):
        team_Desi = int(input())
        team_opposite = int(input())
        if team_Desi > team_opposite:
            points_Desi = team_Desi - team_opposite
            win_games += 1
            print(f"Game {i} of tournament {tournament}: win with {points_Desi} points.")
        else:
            points_opposite = team_opposite - team_Desi
            print(f"Game {i} of tournament {tournament}: lost with {points_opposite} points.")
        count += 1
    command = input()
    tournament = command
win_perc = (win_games / count) * 100
loose_perc = 100 - win_perc
print(f"{win_perc:.2f}% matches win")
print(f"{loose_perc:.2f}% matches lost")
