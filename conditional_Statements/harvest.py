from math import ceil
from math import floor
area = int(input())
grape_kg_per_meter = float(input())
needed_wine = int(input())
workers = int(input())

grape_kg = area * grape_kg_per_meter
wine_lt = grape_kg * 0.4 / 2.5
wine_left = abs(wine_lt - needed_wine)
per_worker = wine_left / workers

if needed_wine <= wine_lt:
    print(f"Good harvest this year! Total wine: {int(ceil(wine_lt))} liters.")
    print(f"{int(ceil(wine_left))} liters left -> {ceil(per_worker)} liters per person.")
else:
    print(f"It will be a tough winter! More {int(floor(wine_left))} liters wine needed.")