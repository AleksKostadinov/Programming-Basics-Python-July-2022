n_square = int(input())
w_tile = float(input())
l_tile = float(input())
m_bench = int(input())
o_bench = int(input())

square = n_square * n_square
bench = m_bench * o_bench
square_without_bench = square - bench
tile = w_tile * l_tile

total_tiles = square_without_bench / tile
time = total_tiles * 0.2

print(round(total_tiles, 2))
print(round(time, 2))
