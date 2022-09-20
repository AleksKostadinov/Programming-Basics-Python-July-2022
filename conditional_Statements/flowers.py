hrisantemi = int(input())
rozi = int(input())
laleta = int(input())
season = input()
holiday = input()
decrease = 1
all_flowers = hrisantemi + rozi + laleta
arange = 2

if season == "Spring" or season == "Summer":
    hrisantemi_price = 2
    rozi_price = 4.1
    laleta_price = 2.5
    if laleta > 7 and season == "Spring":
        decrease = 1 - 0.05
    else:
        decrease = 1
elif season == "Autumn" or season == "Winter":
    hrisantemi_price = 3.75
    rozi_price = 4.5
    laleta_price = 4.15
    if rozi >= 10 and season == "Winter":
        decrease = 1 - 0.10
    else:
        decrease = 1
if all_flowers > 20:
    decrease_plus = 1 - 0.20
else:
    decrease_plus = 1

if holiday == "Y":
    increase_holiday = 1 + 0.15
else:
    increase_holiday = 1

price = hrisantemi * hrisantemi_price + rozi * rozi_price + laleta * laleta_price
total_price = price * increase_holiday * decrease * decrease_plus + arange
print(f"{total_price:.2f}")
