number_joinery = int(input())
type_joinery = input()
delivery = input()
tax_delivery = 0
price_for_one = 0

while number_joinery >= 10:

    if type_joinery == "90X130":
        price_for_one = 110
        if number_joinery > 60:
            price_for_one *= 0.92
        elif number_joinery > 30:
            price_for_one *= 0.95
    elif type_joinery == "100X150":
        price_for_one = 140
        if number_joinery > 80:
            price_for_one *= 0.9
        elif number_joinery > 40:
            price_for_one *= 0.94
    elif type_joinery == "130X180":
        price_for_one = 190
        if number_joinery > 50:
            price_for_one *= 0.88
        elif number_joinery > 20:
            price_for_one *= 0.93
    elif type_joinery == "200X300":
        price_for_one = 250
        if number_joinery > 50:
            price_for_one *= 0.86
        elif number_joinery > 25:
            price_for_one *= 0.91

    if delivery == "With delivery":
        tax_delivery += 60

    total = price_for_one * number_joinery + tax_delivery
    if number_joinery > 99:
        total *= 0.96

    print(f"{total:.2f} BGN")
    break
else:
    print(f"Invalid order")