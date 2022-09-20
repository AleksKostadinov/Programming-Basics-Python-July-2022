country = input()
dates = input()
nights = int(input())

if country == "France":
    if dates == "21-23":
        price = 30
    elif dates == "24-27":
        price = 35
    else:
        price = 40
elif country == "Italy":
    if dates == "21-23":
        price = 28
    elif dates == "24-27":
        price = 32
    else:
        price = 39
else:
    if dates == "21-23":
        price = 32
    elif dates == "24-27":
        price = 37
    else:
        price = 43
cost = price * nights
print(f"Easter trip to {country} : {cost:.2f} leva.")
