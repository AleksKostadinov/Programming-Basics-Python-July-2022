x = float(input())
y = float(input())
h = float(input())

#wall
wall = x * y
window = 1.5 * 1.5
side_walls = wall * 2 - window * 2
back_wall = x * x
entry = 1.2 * 2
fb_walls = back_wall * 2 - entry
total_walls = side_walls + fb_walls
green_paint = total_walls / 3.4

#roof
square = x * y
triangle = x * h / 2
total_roof = square * 2 + triangle * 2
red_paint = total_roof / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')