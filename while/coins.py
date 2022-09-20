change = float(input())
change_to_st = round(change * 100)
counter_coins = 0

while change_to_st > 0:
    if change_to_st >= 200:
        change_to_st -= 200
    elif change_to_st >= 100:
        change_to_st -= 100
    elif change_to_st >= 50:
        change_to_st -= 50
    elif change_to_st >= 20:
        change_to_st -= 20
    elif change_to_st >= 10:
        change_to_st -= 10
    elif change_to_st >= 5:
        change_to_st -= 5
    elif change_to_st >= 2:
        change_to_st -= 2
    elif change_to_st >= 1:
        change_to_st -= 1
    counter_coins += 1

print(counter_coins)