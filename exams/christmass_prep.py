number_paper = int(input())
number_textile = int(input())
liters_glue = float(input())
perc_discount = int(input())

price = (number_paper * 5.8 + number_textile * 7.2 + liters_glue * 1.2) * (1 - perc_discount / 100)

print(f"{price:.3f}")
