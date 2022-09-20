#https://judge.softuni.org/Contests/Practice/Index/1720#0
number = input()

largest_number = sorted(number, reverse=True)
for i in largest_number:
    print(i, end="")