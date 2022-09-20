import math
figure = input()
a = float(input())


#square
if figure == "square":
    area = a * a
    print(f'{area:.3f}')
#rectangle
if figure == "rectangle":
    b = float(input())
    area = a * b
    print(f'{area:.3f}')
#circle
if figure == "circle":
    area = math.pi * a ** 2
    print(f'{area:.3f}')
#triangle
if figure == "triangle":
    b = float(input())
    area = 1/2 * a * b
    print(f'{area:.3f}')
