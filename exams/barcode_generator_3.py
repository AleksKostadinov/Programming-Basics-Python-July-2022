start_num = input()
final_num = input()

for a in range(int(start_num[0]), int(final_num[0]) + 1):
    for b in range(int(start_num[1]), int(final_num[1]) + 1):
        for c in range(int(start_num[2]), int(final_num[2]) + 1):
            for d in range(int(start_num[3]), int(final_num[3]) + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f'{a}{b}{c}{d}', end=' ')