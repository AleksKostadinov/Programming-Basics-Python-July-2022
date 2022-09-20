from math import floor

n = int(input())

# begin
print("*" * (n * 2) + " " * n + (n * 2) * "*")

# middle
for i in range(0, n - 2):

    if i == floor(((n - 2) - 1) / 2):
        print("*" + "/" * ((2 * n) - 2) + "*" + "|" * n + "*" + "/" * ((2 * n) - 2) + "*")
    else:
        print("*" + "/" * ((2 * n) - 2) + "*" + " " * n + "*" + "/" * ((2 * n) - 2) + "*")

# end
print("*" * (n * 2) + " " * n + (n * 2) * "*")
