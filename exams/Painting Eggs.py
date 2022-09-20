size_eggs = input()
colour_eggs = input()
couple_eggs = int(input())

if size_eggs == "Large":
    if colour_eggs == "Red":
        price = 16
    elif colour_eggs == "Green":
        price = 12
    else:
        price = 9
elif size_eggs == "Medium":
    if colour_eggs == "Red":
        price = 13
    elif colour_eggs == "Green":
        price = 9
    else:
        price = 7
else:
    if colour_eggs == "Red":
        price = 9
    elif colour_eggs == "Green":
        price = 8
    else:
        price = 5
cost = price * couple_eggs * 0.65
print(f"{cost:.2f} leva.")