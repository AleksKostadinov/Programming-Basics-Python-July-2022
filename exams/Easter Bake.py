from math import ceil
num_bread = int(input())
total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0
for bread in range(1, num_bread + 1):
    sugar_gr = int(input())
    flour_gr = int(input())
    if sugar_gr >= max_sugar:
        max_sugar = sugar_gr
    if flour_gr >= max_flour:
        max_flour = flour_gr

    total_sugar += sugar_gr
    total_flour += flour_gr

packet_sugar = ceil(total_sugar / 950)
packet_flour = ceil(total_flour / 750)

print(f"Sugar: {packet_sugar}")
print(f"Flour: {packet_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")