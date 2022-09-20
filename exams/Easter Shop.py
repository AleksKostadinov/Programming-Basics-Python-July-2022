start_eggs = int(input())

count = 0
while True:
    command = input()
    if command == "Close":
        print(f"Store is closed!")
        print(f"{count} eggs sold.")
        break
    number_eggs = int(input())

    if command == "Buy":
        if start_eggs >= number_eggs:
            start_eggs -= number_eggs
            count += number_eggs
        elif start_eggs < number_eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {start_eggs}.")
            break
    elif command == "Fill":
        start_eggs += number_eggs