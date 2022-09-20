days = int(input())
types = input()
rating = input()

room_for_person = 18
apartment = 25
president_apartment = 35

d_apartment = 0
d_rating = 0
price = 0

if types == "apartment":
    types = 25
    if days < 10:
        d_apartment = 1 - 0.30
    elif 10 <= days <= 15:
        d_apartment = 1 - 0.35
    else:
        d_apartment = 1 - 0.5

elif types == "president apartment":
    types = 35
    if days < 10:
        d_apartment = 1 - 0.1
    elif 10 <= days <= 15:
        d_apartment = 1 - 0.15
    else:
        d_apartment = 1 - 0.20

else:
    types = 18
    d_apartment = 1

if rating == "positive":
    d_rating = 1 + 0.25
else:
    d_rating = 1 - 0.1

price = (days - 1) * types * d_apartment * d_rating

print(f"{price:.2f}")
