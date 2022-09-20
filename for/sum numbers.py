loops = int(input("Amount of loops: "))
lis = []

for i in range(loops):
    numbers = int(input("Input: "))
    lis.append(numbers)

print(sum(lis))