num_1 = int(input())
letter_2 = input()
letter_3 = input()
num_4 = int(input())
num_5 = int(input())
num_6 = int(input())
position = int(input())
count = 0
result = ""
cycle_end = False
for a in range(1, num_1 + 1):
    for b in range(65, ord(letter_2.upper()) + 1):
        for c in range(97, ord(letter_3.lower()) + 1):
            for d in range(1, num_4 + 1):
                for e in range(1, num_5 + 1):
                    for f in range(1, num_6 + 1):
                        count += 1
                        if position == count:
                            result = str(a) + chr(b) + chr(c) + str(d) + str(e) + str(f)
                            cycle_end = True
                            break
                        elif count > position:
                            cycle_end = False
                            break
                    if cycle_end:
                        break
                if cycle_end:
                    break
            if cycle_end:
                break
        if cycle_end:
            break
    if cycle_end:
        break
if cycle_end:
    print(result)
else:
    print("No password on this position")