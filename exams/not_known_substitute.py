first = int(input())
second = int(input())
third = int(input())
fourth = int(input())
count = 0
no_more_changes = False
for a in range(first, 8 + 1):
    for b in range(9, second - 1, -1):
        for c in range(third, 8 + 1):
            for d in range(9, fourth - 1, -1):
                if a % 2 == 0 and c % 2 == 0 and b % 2 != 0 and d % 2 != 0:
                    if str(a) + str(b) != str(c) + str(d):
                        count += 1
                        print(f"{a}{b} - {c}{d}")
                    else:
                        print(f"Cannot change the same player.")
                    if count == 6:
                        no_more_changes = True
                        break
                if no_more_changes:
                    break
            if no_more_changes:
                break
        if no_more_changes:
            break
    if no_more_changes:
        break
