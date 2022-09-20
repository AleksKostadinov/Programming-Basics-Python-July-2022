price_luggage = float(input())
kg_luggage = float(input())
days_departure = int(input())
number_luggage = int(input())

if kg_luggage < 10:
    price_luggage *= 0.2
elif kg_luggage <= 20:
    price_luggage *= 0.5
# else:
#     pass

if days_departure < 7:
    price_luggage *= 1.4
elif days_departure <= 30:
    price_luggage *= 1.15
else:
    price_luggage *= 1.1
total_price = price_luggage * number_luggage

print(f" The total price of bags is: {total_price:.2f} lv. ")
