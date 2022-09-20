stadium_cap = int(input())
total_fans = int(input())
a = 0
b = 0
v = 0
g = 0
for i in range(1, total_fans + 1):
    fan = input()

    if fan == "A":
        a += 1
    elif fan == "B":
        b += 1
    elif fan == "V":
        v += 1
    elif fan == "G":
        g += 1

print(f"{a / total_fans * 100:.2f}%")
print(f"{b / total_fans * 100:.2f}%")
print(f"{v / total_fans * 100:.2f}%")
print(f"{g / total_fans * 100:.2f}%")
print(f"{total_fans / stadium_cap * 100:.2f}%")
