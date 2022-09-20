price_veg = float(input())
price_fru = float(input())
kilo_veg = int(input())
kilo_fru = int(input())

veg = price_veg * kilo_veg
fru = price_fru * kilo_fru

total = (veg + fru) / 1.94
print(total)