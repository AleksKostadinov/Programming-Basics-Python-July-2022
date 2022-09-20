flowers = input()
pieces = int(input())
budget = int(input())
price = 0

Roses = 5.00
Dahlias = 3.80
Tulips = 2.80
Narcissus = 3.00
Gladiolus = 2.50

discount_Roses = 10/100
discount_Dahlias = 15/100
discount_Tulips = 15/100
discount_Narcissus = 15/100
discount_Gladiolus = 20/100

if flowers == "Roses":
    if pieces > 80:
        price = pieces * Roses * (1 - discount_Roses)
    else:
        price = pieces * Roses

elif flowers == "Dahlias":
    if pieces > 90:
        price = pieces * Dahlias * (1 - discount_Dahlias)
    else:
        price = pieces * Dahlias

elif flowers == "Tulips":
    if pieces > 80:
        price = pieces * Tulips * (1 - discount_Tulips)
    else:
        price = pieces * Tulips

elif flowers == "Narcissus":
    if pieces < 120:
        price = pieces * Narcissus * (1 + discount_Narcissus)
    else:
        price = pieces * Narcissus

elif flowers == "Gladiolus":
    if pieces < 80:
        price = pieces * Gladiolus * (1 + discount_Gladiolus)
    else:
        price = pieces * Gladiolus

enough_budget = budget - price
not_enough_budget = price - budget

if budget >= price:
    print(f"Hey, you have a great garden with {pieces} {flowers} and {enough_budget:.2f} leva left.")

else:
    print(f'Not enough money, you need {not_enough_budget:.2f} leva more.')