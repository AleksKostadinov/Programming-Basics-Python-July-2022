#https://judge.softuni.org/Contests/Practice/Index/1720#2
array = input().split(", ")

if array.pop() == "wolf":
    print("Please go away and stop eating my sheep")
    raise SystemExit

arrReversed = array[::-1]

for i in range(len(arrReversed)):
    if arrReversed[i] != "sheep":
        print(f"Oi! Sheep number {i + 1}! You are about to be eaten by a wolf!")