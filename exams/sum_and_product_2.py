n = int(input())
found_combination = False
for a in range(1, 9 + 1):
    for b in range(9, a - 1, - 1):
        for c in range(0, 9 + 1):
            for d in range(9, c - 1, - 1):
                sum_abcd = a + b + c + d
                multiply_abcd = a * b * c * d
                string_abcd = str(a) + str(b) + str(c) + str(d)
                string_dcba = "".join(reversed(string_abcd))
                if sum_abcd == multiply_abcd and n % 10 == 5:
                    print(string_abcd)
                    found_combination = True
                    break
                elif multiply_abcd // sum_abcd == 3 and n % 3 == 0:
                    print(string_dcba)
                    found_combination = True
                    break
            if found_combination:
                break
        if found_combination:
            break
    if found_combination:
        break
if not found_combination:
    print("Nothing found")