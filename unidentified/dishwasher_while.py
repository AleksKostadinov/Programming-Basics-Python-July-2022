bottles = int(input())
cup = 0
plate = 0
n = 0
quantity_def = 750 * bottles

while quantity_def >= 0:
    dishes_n = input()
    n += 1
    if dishes_n == "End":
        break
    if n % 3 == 0:
        quantity_def -= int(dishes_n) * 15
        cup += int(dishes_n)

    else:
        quantity_def -= int(dishes_n) * 5
        plate += int(dishes_n)

if quantity_def >= 0:
    print('Detergent was enough!')
    print(f'{plate} dishes and {cup} pots were washed.')
    print(f'Leftover detergent {quantity_def} ml.')
else:
    print(f'Not enough detergent, {abs(quantity_def)} ml. more necessary!')