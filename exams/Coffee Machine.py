type_drinks = input()
sugar = input()
number_drinks = int(input())
discount = 1

if type_drinks == "Espresso":
    if sugar == "Without":
        price = 0.9
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.2
elif type_drinks == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.2
    elif sugar == "Extra":
        price = 1.6
elif type_drinks == "Tea":
    if sugar == "Without":
        price = 0.5
    elif sugar == "Normal":
        price = 0.6
    elif sugar == "Extra":
        price = 0.7
total_wo_discount = (price * number_drinks)
if sugar == "Without":
    total_wo_discount *= 0.65
if type_drinks == "Espresso":
    if number_drinks >= 5:
        total_wo_discount *= 0.75
if total_wo_discount > 15:
    total_wo_discount *= 0.8

total = total_wo_discount * discount
print(f"You bought {number_drinks} cups of {type_drinks} for {total:.2f} lv.")
