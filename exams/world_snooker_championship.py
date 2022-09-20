

stage = input()
type_ticket = input()
number_tickets = int(input())
photos = input()
price_ticket = 0
total = 0
discount = 1
if stage == "Quarter final":
    if type_ticket == "Standard":
        price_ticket += 55.50
    elif type_ticket == "Premium":
        price_ticket += 105.20
    elif type_ticket == "VIP":
        price_ticket += 118.9
elif stage == "Semi final":
    if type_ticket == "Standard":
        price_ticket += 75.88
    elif type_ticket == "Premium":
        price_ticket += 125.22
    elif type_ticket == "VIP":
        price_ticket += 300.40
elif stage == "Final":
    if type_ticket == "Standard":
        price_ticket += 110.10
    elif type_ticket == "Premium":
        price_ticket += 160.66
    elif type_ticket == "VIP":
        price_ticket += 400

total = price_ticket * number_tickets

if total > 4000:
    total *= 0.75

elif total > 2500:
    total *= 0.90
    if photos == "Y":
        total += 40 * number_tickets
else:
    if photos == "Y":
        total += 40 * number_tickets

print(f"{total:.2f}")
