from math import floor
holidays = int(input())

workdays = 365 - holidays
play_min = workdays * 63 + holidays * 127
total = abs(30000 - play_min)
h = floor(total // 60)
m = floor(total % 60)

if play_min > 30000:
  print("Tom will run away")
  print(f"{h} hours and {m} minutes more for play")
else:
  print("Tom sleeps well")
  print(f"{h} hours and {m} minutes less for play")