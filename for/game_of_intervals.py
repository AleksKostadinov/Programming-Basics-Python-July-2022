num_moves = int(input())
is_valid = True
result = 0
sum_number = 0
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0

for move in range(1, num_moves + 1):
    new_number = float(input())

    if new_number < 0 or new_number > 50:
        sum_number /= 2
        f += 1
    elif new_number <= 9:
        sum_number += new_number * 0.2
        a += 1
    elif new_number <= 19:
        sum_number += new_number * 0.3
        b += 1
    elif new_number <= 29:
        sum_number += new_number * 0.4
        c += 1
    elif new_number <= 39:
        sum_number += 50
        d += 1
    elif new_number <= 50:
        sum_number += 100
        e += 1

print(f'{sum_number:.2f}')
print(f"From 0 to 9: {(a / num_moves * 100):.2f}%")
print(f"From 10 to 19: {(b / num_moves * 100):.2f}%")
print(f"From 20 to 29: {(c / num_moves * 100):.2f}%")
print(f"From 30 to 39: {(d / num_moves * 100):.2f}%")
print(f"From 40 to 50: {(e / num_moves * 100):.2f}%")
print(f"Invalid numbers: {(f / num_moves * 100):.2f}%")
