months = int(input())
energy = 0
other_per_month = 0
for i in range(1, months + 1):
    energy_per_month = float(input())

    energy += energy_per_month
    other_per_month += (energy_per_month + 20 + 15) * 1.2

water = months * 20
inet = months * 15
average_per_month = (energy + water + inet + other_per_month) / months

print(f"Electricity: {energy:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {inet:.2f} lv")
print(f"Other: {other_per_month:.2f} lv")
print(f"Average: {average_per_month:.2f} lv")


