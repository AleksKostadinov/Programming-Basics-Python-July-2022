from math import floor
h = float(input()) * 100
w = float(input()) * 100

width = (w - 100) // 70
height = h // 120
area = floor(width * height)
total = area - 3

print(total)