n = int(input())
count = 0
is_4 = False
password = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    if n == (a * b + c * d):
                        count += 1
                        result = str(a) + str(b) + str(c) + str(d)
                        print(result, end=" ")
                        if count == 4:
                            password = result
                            is_4 = True
if is_4:
    print()
    print(f"Password: {password}")
if count < 3:
    print("\nNo!")
