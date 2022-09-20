input_num = input()
max = -10000000000000

while input_num != "Stop":
    num = int(input_num)
    if num > max:
        max = num
    input_num = input()

print(max)