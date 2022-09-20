num_locations = int(input())

for location in range(num_locations):
    expected_avg_gold = float(input())
    days_per_location = int(input())
    gold = 0
    for day in range(days_per_location):
        gold_per_day = float(input())
        gold += gold_per_day
    avg_gold_day = gold / days_per_location

    if avg_gold_day >= expected_avg_gold:
        print(f"Good job! Average gold per day: {avg_gold_day:.2f}.")
    else:
        diff = expected_avg_gold - avg_gold_day
        print(f"You need {diff:.2f} gold.")