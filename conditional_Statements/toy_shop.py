price_tour = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())
discount = 0
toys = puzzle + doll + bear + minion + truck
prices = puzzle * 2.60 + doll * 3.00 + bear * 4.10 + minion * 8.20 + truck * 2.00
if toys >= 50:
    discount = prices * 25 / 100

profit = prices - discount

total = profit * (1 - 10/100)

enough_money = abs(total - price_tour)
if price_tour <= total:
    print(f"Yes! {enough_money:.2f} lv left.")

else:
    print(f"Not enough money! {enough_money:.2f} lv needed.")