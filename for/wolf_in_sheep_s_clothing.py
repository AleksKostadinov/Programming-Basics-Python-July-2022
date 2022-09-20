#https://judge.softuni.org/Contests/Practice/Index/1720#2
animals = input().split(", ")

animals_list = []
for animal in animals:
    animals_list.append(animal)

if animals_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    animal_position = len(animals_list) - animals_list.index("wolf") - 1
    print(f"Oi! Sheep number {animal_position}! You are about to be eaten by a wolf!")