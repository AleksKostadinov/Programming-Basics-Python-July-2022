divisor = int(input())
boundary = int(input())
max_num = 0
for i in range(divisor, boundary + 1):
    if i % divisor == 0:
        if i > max_num:
            max_num = i
print(max_num)