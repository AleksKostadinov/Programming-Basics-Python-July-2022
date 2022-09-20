session = input()
type_contract = input()
extra_net = input()
num_months = int(input())
discount = 1
if session == "one":
    if type_contract == "Small":
        tax = 9.98
    elif type_contract == "Middle":
        tax = 18.99
    elif type_contract == "Large":
        tax = 25.98
    else:
        tax = 35.99
else:
    if type_contract == "Small":
        tax = 8.58
    elif type_contract == "Middle":
        tax = 17.09
    elif type_contract == "Large":
        tax = 23.59
    else:
        tax = 31.79

if extra_net == "yes":
    if tax <= 10:
        tax += 5.5
    elif tax <= 30:
        tax += 4.35
    else:
        tax += 3.85
if session == "two":
    discount = 1 - 0.0375
price = (tax * num_months) * discount
print(f"{price:.2f} lv.")
