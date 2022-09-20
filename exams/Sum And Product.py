n = int(input())
is_not_found = True
for a in range(1, 9 + 1):
    for b in range(9, a - 1, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c - 1, -1):
                sum_abcd = a + b + c + d
                product_abcd = a * b * c * d
                if sum_abcd == product_abcd and n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    is_not_found = False
                    break
                elif product_abcd // sum_abcd == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    is_not_found = False
                    break
            if not is_not_found:
                break
        if not is_not_found:
            break
    if not is_not_found:
        break
if is_not_found:
    print("Nothing found")
