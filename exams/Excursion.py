people_in_group = int(input())
number_of_nights = int(input())
number_cards_for_transport = int(input())
number_tickets_for_museum = int(input())

nights_price = number_of_nights * 20
cards_price = number_cards_for_transport * 1.60
ticket_price = number_tickets_for_museum * 6

price_per_person = nights_price + cards_price + ticket_price
total = (price_per_person * people_in_group) * 1.25

print(f"{total:.2f}")