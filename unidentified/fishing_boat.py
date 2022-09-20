budget = int(input())
season = input()
number = int(input())
discount = 0

if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
else:
    rent = 2600

if number <= 6:
    discount = 0.1
elif 7 <= number <= 11:
    discount = 0.15
else:
    discount = 0.25

price = rent * (1 - discount)

if number % 2 == 0 and season != "Autumn":
    price = price * (1 - 0.05)


if budget >= price:
    print(f'Yes! You have {budget - price:.2f} leva left.')

else:
    print(f'Not enough money! You need {abs(price - budget):.2f} leva.')
