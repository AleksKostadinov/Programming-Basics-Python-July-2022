city = input()
type = input()
vip = input()
days = int(input())
discount = 1
isinValid = False
while True:
    if days > 7:
        days -= 1
    if city == "Bansko" or city == "Borovets":
        if type == "withEquipment":
            price = 100
            if vip == "yes":
                discount = 0.9
        elif type == "noEquipment":
            price = 80
            if vip == "yes":
                discount = 0.95
        else:
            isinValid = True
        break
    elif city == "Varna" or city == "Burgas":
        if type == "withBreakfast":
            price = 130
            if vip == "yes":
                discount = 0.88
        elif type == "noBreakfast":
            price = 100
            if vip == "yes":
                discount = 0.93
        else:
            isinValid = True
        break
    else:
        isinValid = True
        break
if isinValid:
    print("Invalid input!")
elif days < 1:
    print(f"Days must be positive number!")
else:
    total = days * price * discount
    print(f"The price is {total:.2f}lv! Have a nice time!")
