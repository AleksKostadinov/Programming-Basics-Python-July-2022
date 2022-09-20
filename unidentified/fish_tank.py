length = float(input())
width = float(input())
height = float(input())
percent = float(input())
vol = length * width * height
volLitres = vol / 1000
needLitres = volLitres * (1 - percent/100)
print(needLitres)