name_actor = input()
points_acad = float(input())
number_ev = int(input())
points_actor = 0
total_points = 0

for i in range(number_ev):
    name_ev = input()
    point_ev = float(input())

    points_actor += (len(name_ev) * point_ev / 2)

    total_points = points_actor + points_acad
    if total_points > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
        break
if total_points < 1250.5:
    print(f"Sorry, {name_actor} you need {abs(1250.5 - total_points):.1f} more!")
