import math
record_seconds = float(input())
meters = float(input())
sec_per_meter = float(input())
ivan_sec_swim = meters * sec_per_meter
sec_resist = math.floor(meters / 15) * 12.5
ivan_total = ivan_sec_swim + sec_resist
difference = record_seconds - ivan_total
if ivan_total >= record_seconds:
    print(f"No, he failed! He was {abs(difference):.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {ivan_total:.2f} seconds.")