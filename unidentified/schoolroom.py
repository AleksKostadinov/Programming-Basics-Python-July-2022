import math

length = float(input()) * 100
width = float(input()) * 100

column = length / 120
row = (width - 100) / 70
trunc_column = math.trunc(column)
trunc_row = math.trunc(row)

places = trunc_row * trunc_column - 3

print(f'{places:0.0f}')