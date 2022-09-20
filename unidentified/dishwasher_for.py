import sys

ml = int(input()) * 750
pc_pl = 0
pc_wok = 0

for n in range(1, sys.maxsize):
    zarezhdane = input()
    if zarezhdane == 'End':
        break
    if n % 3 == 0:
        ml -= int(zarezhdane) * 15
        pc_wok += int(zarezhdane)
    else:
        ml -= int(zarezhdane) * 5
        pc_pl += int(zarezhdane)
    if ml < 0:
        break

if ml >= 0:
    print('Detergent was enough!')
    print(f'{pc_pl} dishes and {pc_wok} pots were washed.')
    print(f'Leftover detergent {ml} ml.')
else:
    print(f'Not enough detergent, {abs(ml)} ml. more necessary!')