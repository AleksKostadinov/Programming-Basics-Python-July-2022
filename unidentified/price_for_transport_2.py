kilometers = int(input())
time_of_day = input()

taxi = 0.70
taxi_daily = 0.79
taxi_night = 0.90
bus = 0.09
distance_bus = 20
train = 0.06
distance_train = 100
price = 0

if kilometers < 20:
    if time_of_day == "day":
        price = (kilometers * taxi_daily) + taxi
if kilometers < 20:
    if time_of_day == "night":
        price = (kilometers * taxi_night) + taxi
elif kilometers < 100:
    if time_of_day == "day" or time_of_day == "night":
        price = (kilometers * bus)
elif kilometers >= 100:
    if time_of_day == "day" or time_of_day == "night":
        price = (kilometers * train)

print(f"{price:.2f}")