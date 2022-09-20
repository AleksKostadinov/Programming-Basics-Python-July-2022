first_part = int(input())
second_part = int(input())
diff_first = int(input())
diff_second = int(input())

for first in range(first_part, first_part + diff_first + 1):
    count_i = 0
    prime_i = 0
    is_prime_i = False
    is_prime_j = False
    for i in range(1, first_part + diff_first + 1):
        if first % i == 0:
            count_i += 1
            if count_i > 2:
                break
    if count_i < 3:
        prime_i = first
        is_prime_i = True
    for second in range(second_part, second_part + diff_second + 1):
        count_j = 0
        prime_j = 0

        is_prime_j = False
        for j in range(1, second_part + diff_second + 1):
            if second % j == 0:
                count_j += 1
                if count_j > 2:
                    break
        if count_j < 3:
            prime_j = second
            is_prime_j = True
        if is_prime_i and is_prime_j:
            print(f"{prime_i}{prime_j}")