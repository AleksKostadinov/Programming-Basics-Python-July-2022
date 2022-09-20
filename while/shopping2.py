budget = int(input())
command = input()

while command != "End":
    number = int(command)
    budget -= number
    if budget < 0:
        print(f"You went in overdraft!")
        break

    command = input()
else:
    print(f"You bought everything needed.")