needed_money = float(input())
money_at_moment = float(input())
total_count_days = 0
count_spend = 0
can_save = True

while money_at_moment < needed_money:
    spend_save = input()
    amount_spend_save = float(input())
    total_count_days += 1

    if spend_save == "save":
        money_at_moment += amount_spend_save
        count_spend = 0
    elif spend_save == "spend":
        money_at_moment -= amount_spend_save
        if money_at_moment < 0:
            money_at_moment = 0
        count_spend += 1
        if count_spend >= 5:
            can_save = False
            break

if can_save:
    print(f"You saved the money for {total_count_days} days.")
else:
    print('You can\'t save the money.')
    print(f"{total_count_days}")
