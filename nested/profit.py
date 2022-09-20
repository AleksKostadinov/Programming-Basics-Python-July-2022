coins_1 = int(input()) #3
coins_2 = int(input()) #2
bank_1 = int(input()) #3
amount = int(input()) #10

for i in range(0, coins_1 + 1):
    for j in range(0, coins_2 + 1):
        for k in range(0, bank_1 + 1):
            if i * 1 + j * 2 + k * 5 == amount:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {amount} lv.")