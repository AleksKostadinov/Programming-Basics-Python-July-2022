volume = float(input())
count = 0
command = input()

while command != "End":
    suitcase = float(command)
    count += 1
    if count % 3 == 0:
        suitcase *= 1.1

    volume -= suitcase

    if volume <= 0:
        volume += suitcase
        count -= 1
        print(f"No more space!")
        break

    command = input()

if command == "End":
    print(f"Congratulations! All suitcases are loaded!")

print(f"Statistic: {count} suitcases loaded.")