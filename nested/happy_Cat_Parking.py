days = int(input())
hours = int(input())
park = 0
count_d = 0

total_park = 0
for i in range(1, days + 1):
    count_d += 1
    park = 0
    for j in range(1, hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            park += 2.5
        elif i % 2 != 0 and j % 2 == 0:
            park += 1.25
        else:
            park += 1

    print(f"Day: {count_d} - {park:.2f} leva")
    total_park += park
print(f"Total: {total_park:.2f} leva")