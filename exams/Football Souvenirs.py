team = input()
type_souvenirs = input()
numbers_souvenirs = int(input())
is_valid = True
price = 0
if team == "Argentina":
    if type_souvenirs == "flags":
        price = 3.25
    elif type_souvenirs == "caps":
        price = 7.2
    elif type_souvenirs == "posters":
        price = 5.1
    elif type_souvenirs == "stickers":
        price = 1.25
    else:
        is_valid = False
        print(f"Invalid stock!")
elif team == "Brazil":
    if type_souvenirs == "flags":
        price = 4.2
    elif type_souvenirs == "caps":
        price = 8.5
    elif type_souvenirs == "posters":
        price = 5.35
    elif type_souvenirs == "stickers":
        price = 1.2
    else:
        is_valid = False
        print(f"Invalid stock!")
elif team == "Croatia":
    if type_souvenirs == "flags":
        price = 2.75
    elif type_souvenirs == "caps":
        price = 6.9
    elif type_souvenirs == "posters":
        price = 4.95
    elif type_souvenirs == "stickers":
        price = 1.1
    else:
        is_valid = False
        print(f"Invalid stock!")
elif team == "Denmark":
    if type_souvenirs == "flags":
        price = 3.1
    elif type_souvenirs == "caps":
        price = 6.5
    elif type_souvenirs == "posters":
        price = 4.8
    elif type_souvenirs == "stickers":
        price = 0.9
    else:
        is_valid = False
        print(f"Invalid stock!")
else:
    is_valid = False
    print(f"Invalid country!")
total_price = price * numbers_souvenirs
if is_valid:
    print(f'Pepi bought {numbers_souvenirs} {type_souvenirs} of {team} for {total_price:.2f} lv.')