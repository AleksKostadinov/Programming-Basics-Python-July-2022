n1 = int(input())
n2 = int(input())
operator = input()

if operator == "+":
    gathering = n1 + n2
    if gathering % 2 == 0:
        print(f"{n1} + {n2} = {gathering} - even")
    else:
        print(f"{n1} + {n2} = {gathering} - odd")
elif operator == "-":
    subtraction = n1 - n2
    if subtraction % 2 == 0:
        print(f"{n1} - {n2} = {subtraction} - even")
    else:
        print(f"{n1} - {n2} = {subtraction} - odd")
elif operator == "*":
    multiplication = n1 * n2
    if multiplication % 2 == 0:
        print(f"{n1} * {n2} = {multiplication} - even")
    else:
        print(f"{n1} * {n2} = {multiplication} - odd")
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        division = n1 / n2
        print(f"{n1} / {n2} = {division:.2f}")
else:
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        modular_division = n1 % n2
        print(f"{n1} % {n2} = {modular_division}")