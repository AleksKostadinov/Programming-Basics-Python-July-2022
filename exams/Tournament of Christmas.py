days = int(input())
win_day = 0
total_price = 0
for day in range(days):
    command = input()
    win_count_day = 0
    lose_count_day = 0
    day_price = 0
    while command != "Finish":

        win_lose = input()
        if win_lose == "win":
            day_price += 20
            win_count_day += 1
        elif win_lose == "lose":
            lose_count_day += 1

        command = input()

    if win_count_day > lose_count_day:
        day_price *= 1.1
        win_day += 1
    else:
        win_day -= 1

    total_price += day_price

if win_day > 0:
    total_price *= 1.2
    print(f"You won the tournament! Total raised money: {total_price:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {abs(total_price):.2f}")