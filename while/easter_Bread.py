from math import ceil
budget = float(input())
flour_kg_price = float(input())
total_loaf = 0
colored_eggs = 0
price_pack_eggs = flour_kg_price * 0.75
l_milk = flour_kg_price * 1.25
q_milk = l_milk / 4
loaf = price_pack_eggs + flour_kg_price + q_milk

while budget > loaf:
    budget -= loaf
    total_loaf += 1
    colored_eggs += 3
    if total_loaf % 3 == 0:
        colored_eggs -= total_loaf - 2
print(f"You made {total_loaf} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")