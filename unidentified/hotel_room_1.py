month = input()
number = int(input())
apartment_discount = 0.00
studio_discount = 0.00

if month == "May" or month == "October":
    studio = 50.00
    apartment = 65.00
    if 7 < number <= 14:
        studio_discount = studio * 0.05
    elif number > 14:
        studio_discount = studio * 0.30
        apartment_discount = apartment * 0.1
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if number > 14:
        studio_discount = studio * 0.20
        apartment_discount = apartment * 0.1
elif month == "July" or month == "August":
    studio = 76.00
    apartment = 77.00
    if number > 14:
        apartment_discount = apartment * 0.1
ap_cost = apartment - apartment_discount
st_cost = studio - studio_discount

print(f"Apartment: {number * (apartment - apartment_discount):.2f} lv.")
print(f"Studio: {number * (studio - studio_discount):.2f} lv.")