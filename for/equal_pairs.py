num = int(input())

last_pair_sum = 0
current_pair_sum = 0
diff = 0
maxdiff = 0

for i in range(1, num + 1):
    first_num = int(input())
    second_num = int(input())

    if i == 1:
        last_pair_sum = first_num + second_num
    else:
        current_pair_sum = first_num + second_num
        diff = abs(current_pair_sum - last_pair_sum)
        if diff > maxdiff:
            maxdiff = diff
        last_pair_sum = current_pair_sum

if maxdiff == 0:
    print(f"Yes, value={last_pair_sum}")
else:
    print(f"No, maxdiff={maxdiff}")