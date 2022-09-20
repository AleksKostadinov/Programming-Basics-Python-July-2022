from math import floor

first = int(input())
second = int(input())
third = int(input())

summ = first + second + third
minutes = summ // 60
seconds = summ % 60
minutes = floor(minutes)
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f"{minutes}:{seconds}")