capacity = int(input())
command = input()
price = 0
while command != "Movie time!":
    people = int(command)
    capacity -= people
    if capacity < 0:
        print(f"The cinema is full.")
        break

    price += people * 5

    if people % 3 == 0:
        price -= 5

    command = input()
if capacity >= 0:
    print(f"There are {capacity} seats left in the cinema.")

print(f"Cinema income - {price} lv.")
