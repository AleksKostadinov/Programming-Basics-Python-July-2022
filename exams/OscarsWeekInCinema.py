movie = input()
type_hall = input()
number_tickets = int(input())
ticket_price = 0

if type_hall == "normal":
    if movie == "A Star Is Born":
        ticket_price = 7.50
    elif movie == "Bohemian Rhapsody":
        ticket_price = 7.35
    elif movie == "Green Book":
        ticket_price = 8.15
    elif movie == "The Favourite":
        ticket_price = 8.75
elif type_hall == "luxury":
    if movie == "A Star Is Born":
        ticket_price = 10.5
    elif movie == "Bohemian Rhapsody":
        ticket_price = 9.45
    elif movie == "Green Book":
        ticket_price = 10.25
    elif movie == "The Favourite":
        ticket_price = 11.55
elif type_hall == "ultra luxury":
    if movie == "A Star Is Born":
        ticket_price = 13.5
    elif movie == "Bohemian Rhapsody":
        ticket_price = 12.75
    elif movie == "Green Book":
        ticket_price = 13.25
    elif movie == "The Favourite":
        ticket_price = 13.95
total = ticket_price * number_tickets
print(f"{movie} -> {total:.2f} lv.")