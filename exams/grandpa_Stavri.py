number_days = int(input())
degrees_rakia = 0
current_degrees_rakia = 0
total_rakia = 0
for day in range(1, number_days + 1):
    liters_rakia = float(input())
    degrees_rakia = float(input())
    current_liters = liters_rakia
    total_rakia += liters_rakia
    current_degrees_rakia += current_liters * degrees_rakia
avg_degrees = current_degrees_rakia / total_rakia

print(f"Liter: {total_rakia:.2f}")
print(f"Degrees: {avg_degrees:.2f}")
if avg_degrees < 38:
    print(f"Not good, you should baking!")
elif avg_degrees <= 42:
    print(f"Super!")
else:
    print(f"Dilution with distilled water!")