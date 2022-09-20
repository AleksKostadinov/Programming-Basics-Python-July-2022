# https://judge.softuni.org/Contests/Compete/Index/1719#7
command = input()
total_coffee = 0
while command != "END":
    if command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        total_coffee += 2

    elif command == "coding" or command == "dog" or command == "cat" or command == "movie":
        total_coffee += 1

    else:
        pass
    command = input()
if command == "END":
    if total_coffee > 5:
        print(f"You need extra sleep")
    else:
        print(total_coffee)
