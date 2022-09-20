#https://judge.softuni.org/Contests/Practice/Index/1060#2
bought_hr = int(input())
bought_roses = int(input())
bought_lal = int(input())
season = input()
holiday = input()
flower_price = 1
total_flowers = bought_hr + bought_lal + bought_roses

if season == "Summer" or season == "Spring":
    flower_price = ((bought_hr * 2) + (bought_lal * 2.5) + (bought_roses * 4.1))
    if season == "Spring":
        if bought_lal >= 7:
            flower_price *= 0.95
else:
    flower_price = ((bought_hr * 3.75) + (bought_lal * 4.15) + (bought_roses * 4.5))
    if season == "Winter":
        if bought_roses >= 10:
            flower_price *= 0.90

if holiday == "Y":
    flower_price *= 1.15

if total_flowers >= 20:
    flower_price *= 0.8

total_price = flower_price + 2

print(f"{total_price:.2f}")