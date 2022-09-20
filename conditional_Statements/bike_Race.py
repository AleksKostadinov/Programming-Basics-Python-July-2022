junior = int(input())
senior = int(input())
type_t = input()
number = junior + senior
tax = 0

if type_t == "trail":
    type_j = 5.5
    type_s = 7
elif type_t == "cross-country":
    type_j = 8
    type_s = 9.5
    if number >= 50:
        tax = 0.25
elif type_t == "downhill":
    type_j = 12.25
    type_s = 13.75
elif type_t == "road":
    type_j = 20
    type_s = 21.50

tax_or = 1 - 0.05

collect_sum = junior * type_j + senior * type_s

final_sum = collect_sum * tax_or * (1 - tax)

print(f"{final_sum:.2f}")