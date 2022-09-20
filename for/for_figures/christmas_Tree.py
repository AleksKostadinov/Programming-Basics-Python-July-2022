n = int(input())

for i in range(1, n + 2):
    print(" " * (n + 1 - i) + "*" * (i - 1) + " | " + (i - 1) * "*")

#count = int(input())

# for i in range(count + 1):
#     print(f"{' ' * (count - i)}{'*' * i} | {'*' * i}")


