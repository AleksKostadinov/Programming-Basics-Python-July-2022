ticket_type = input()
rows = int(input())
columns = int(input())

tickets = rows * columns
ticket_price = 0

if ticket_type == "Premiere":
    ticket_price = 12.00 * tickets
elif ticket_type == "Normal":
    ticket_price = 7.50 * tickets
elif ticket_type == "Discount":
    ticket_price = 5.00 * tickets

print(f'{ticket_price:.2f} leva')