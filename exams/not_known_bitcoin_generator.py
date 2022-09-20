a = int(input())
b = int(input())
max_tries = int(input())
flag = False
result = ""
count = 0
for A in range(33, 47):
    for B in range(58, 64):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                count += 1
                if count > max_tries:
                    flag = True
                    break
                result = chr(A) + chr(B) + str(x) + str(y) + chr(B) + chr(A)
                print(result, end="|")
                if x == a and y == b:
                    flag = True
                    break
                A += 1
                if A > 47:
                    A = 33
                B += 1
                if B > 64:
                    B = 58
            if flag:
                break
        if flag:
            break
    if flag:
        break
