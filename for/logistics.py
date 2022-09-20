quantity_of_cargo = int(input())
total_weight = 0
price = 0
total_price = 0
bus = 0
truck = 0
train = 0
for i in range(1, quantity_of_cargo + 1):
    weigh_cargo = int(input())

    if weigh_cargo <= 3:  # bus
        price = weigh_cargo * 200
        bus += weigh_cargo
    elif weigh_cargo <= 11:  # truck
        price = weigh_cargo * 175
        truck += weigh_cargo
    else:  # train
        price = weigh_cargo * 120
        train += weigh_cargo

    total_weight += weigh_cargo
    total_price += price

print(f"{total_price / total_weight:.2f}")
print(f"{bus / total_weight * 100:.2f}%")
print(f"{truck / total_weight * 100:.2f}%")
print(f"{train / total_weight * 100:.2f}%")
