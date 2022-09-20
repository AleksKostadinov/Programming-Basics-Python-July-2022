tournament = input()
host_wins = 0
count = 0
while tournament != "End of tournaments":
    number_games = int(input())

    for number in range(1, number_games + 1):
        host_team = int(input())
        guest_team = int(input())
        diff = host_team - guest_team
        count += 1
        if host_team > guest_team:
            host_wins += 1
            print(f"Game {number} of tournament {tournament}: win with {diff} points.")
        elif host_team < guest_team:
            print(f"Game {number} of tournament {tournament}: lost with {abs(diff)} points.")
    tournament = input()

win_rate = (host_wins / count) * 100
lose_rate = 100 - win_rate
print(f"{win_rate:.2f}% matches win\n{lose_rate:.2f}% matches lost")