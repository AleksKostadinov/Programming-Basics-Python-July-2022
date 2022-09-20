#https://judge.softuni.org/Contests/Practice/Index/1060#1
from math import ceil
budget = float(input()) #Събраните пари.
width = float(input()) #Широчината на пода.
length = float(input()) #Дължината на пода.
side_tile = float(input()) #Страната на триъгълника.
h_tile = float(input()) #Височината на триъгълника.
price_tile = float(input()) #Цената на една плочка.
amount = float(input()) #Сумата за майстора.

area = width * length
area_tile = (side_tile * h_tile) / 2
needed_tiles = ceil(area / area_tile) + 5
total_amount = needed_tiles * price_tile + amount
diff = abs(budget - total_amount)

if budget >= total_amount:
	print(f"{diff:.2f} lv left.")
else:
	print(f"You'll need {diff:.2f} lv more.")