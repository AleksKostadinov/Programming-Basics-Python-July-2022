from math import ceil
people = int(input())
tax = float(input())
sunbed = float(input())
umbrella = float(input())

count_umb_2 = people // 2
count_umb_1 = people % 2
count_umbrella = count_umb_2 + count_umb_1

sunbed_count = ceil(people * 0.75)
total = count_umbrella * umbrella + sunbed_count * sunbed + tax * people

print(f"{total:.2f} lv.")