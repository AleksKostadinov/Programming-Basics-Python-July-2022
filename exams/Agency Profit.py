company = input()
number_adult_tickets = int(input())
number_kid_tickets = int(input())
price_adult_ticket_no_tax = float(input())
service_tax = float(input())

price_kid_ticket = price_adult_ticket_no_tax * 0.3 + service_tax

price_adult_ticket = price_adult_ticket_no_tax + service_tax

total_price = number_kid_tickets * price_kid_ticket + number_adult_tickets * price_adult_ticket
profit = total_price * 0.2
print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")
