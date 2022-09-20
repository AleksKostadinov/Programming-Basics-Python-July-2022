first_part = int(input())
second_part = int(input())
diff_first = int(input())
diff_second = int(input())

for a in range(first_part, first_part + diff_first + 1):
    for b in range(second_part, second_part + diff_second + 1):
        if a % 2 != 0 and a % 3 != 0 and a % 5 != 0 and a % 7 != 0 \
                and b % 2 != 0 and b % 3 != 0 and b % 5 != 0 and b % 7 != 0:
            print(f"{a}{b}")