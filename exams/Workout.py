from math import ceil
number_days = int(input())
km_run = float(input())
total = 0
km_run_for_new_day = km_run
count_km_without_1st_day = 0
for day in range(number_days):
    up_distance_percent = int(input())
    up_distance = 1 + (up_distance_percent/100)
    km_run_for_new_day *= up_distance
    count_km_without_1st_day += km_run_for_new_day

total = count_km_without_1st_day + km_run
diff = total - 1000
if total >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(abs(diff))} more kilometers")
