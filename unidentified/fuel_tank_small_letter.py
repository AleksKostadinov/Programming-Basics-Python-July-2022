fuel = input()
liters = int(input())

if fuel == "Diesel" or fuel == "Gasoline" or fuel == "Gas":
    if liters >= 25 and fuel == "Diesel":
        print(f"You have enough diesel.")
    if liters >= 25 and fuel == "Gasoline":
        print(f"You have enough gasoline.")
    if liters >= 25 and fuel == "Gas":
        print(f"You have enough gas.")
    elif liters < 25 and fuel == "Diesel":
        print(f"Fill your tank with diesel!")
    elif liters < 25 and fuel == "Gasoline":
        print(f"Fill your tank with gasoline!")
    elif liters < 25 and fuel == "Gas":
        print(f"Fill your tank with gas!")

else:
    print("Invalid fuel!")
