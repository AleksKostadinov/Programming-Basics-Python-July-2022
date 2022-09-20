number = int(input())
salary = int(input())

for i in range(number):
    name_web = input()
    if name_web == "Facebook":
        salary -= 150
    elif name_web == "Instagram":
        salary -= 100
    elif name_web == "Reddit":
        salary -= 50
    else:
        salary -= 0

if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary}")