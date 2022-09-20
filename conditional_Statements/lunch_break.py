import math

name_of_serial = input()
time_of_serial = int(input())
time_for_break = int(input())

lunch = time_for_break * 1 / 8
relax = time_for_break * 1 / 4

total_time = time_of_serial + lunch + relax

enough_time = math.ceil(time_for_break - total_time)
not_enough_time = math.ceil(total_time - time_for_break)

if time_for_break >= total_time:
    print(f"You have enough time to watch {name_of_serial} and left with {enough_time} minutes free time.")

else:
    print(f"You don't have enough time to watch {name_of_serial}, you need {not_enough_time} more minutes.")