num = int(input())
fact = 1
while True:
    fact *= num
    num -= 1
    if not num > 1:
        break
print(fact)