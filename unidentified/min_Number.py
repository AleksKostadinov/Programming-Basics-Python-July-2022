from sys import maxsize
input_num = input()
min = maxsize

while input_num != "Stop":
    number = int(input_num)
    if number < min:
        min = number
    input_num = input()

print(min)