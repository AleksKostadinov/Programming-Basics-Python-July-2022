#https://judge.softuni.org/Contests/Practice/Index/1060#0
speed_kmh = int(input())
first_time = int(input()) / 60
second_time = int(input()) / 60
third_time = int(input()) / 60

speed_up = speed_kmh * 1.1
speed_down = speed_up * 0.95

distance_1 = speed_kmh * first_time
distance_2 = speed_up * second_time
distance_3 = speed_down * third_time

total_distance = distance_1 + distance_2 + distance_3

print(f'{total_distance:.2f}')