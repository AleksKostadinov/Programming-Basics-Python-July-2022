num_sea = int(input())
num_mountain = int(input())
command = input()
profit = 0
is_sold = False
while command != "Stop":

    if command == "sea":
        profit += 680
        num_sea -= 1
        if num_sea < 0:
            profit -= 680
            num_sea += 1
    elif command == "mountain":
        profit += 499
        num_mountain -= 1
        if num_mountain < 0:
            profit -= 499
            num_mountain += 1
    if num_sea == 0 and num_mountain == 0:
        is_sold = True
        break
    command = input()
if is_sold:
    print(f"Good job! Everything is sold.")

print(f"Profit: {profit} leva.")