actor = input()
points_academy = float(input())
number_of_jury = int(input())
points = 0
total = 0

for jury in range(1, number_of_jury + 1):
    name_of_jury = input()
    points_of_jury = float(input())
    length = len(name_of_jury)
    points += (points_of_jury * length) / 2
    total = points + points_academy

    if total > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {total:.1f}!")
        break

else:
    total -= 1250.5
    print(f"Sorry, {actor} you need {abs(total):.1f} more!")
