budget = int(input())
command = input()
total = 0
while command != "End":
    number = int(command)
    total += number
    if budget >= total:
        command = input()
    else:
        print(f"You went in overdraft!")
        break
else:
    print(f"You bought everything needed.")