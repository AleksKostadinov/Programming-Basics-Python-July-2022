first_number = int(input())
last_number = int(input())
magic_number = int(input())
count = 0
flag = False
for i in range(first_number, last_number + 1):
    for j in range(first_number, last_number + 1):
        count += 1
        if i + j == magic_number:
            print(f"Combination N:{count} ({i} + {j} = {magic_number})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{count} combinations - neither equals {magic_number}")